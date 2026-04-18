#!/usr/bin/env python3
"""
TyC Project Build Script

This Python script provides cross-platform build automation for the TyC project.
It works on Windows, macOS, and Linux.

Usage:
    # On Windows:
    python run.py help
    python run.py setup
    python run.py build
    python run.py test-lexer
    python run.py test-parser
    python run.py test-ast
    python run.py clean

    # On macOS/Linux:
    python3 run.py help
    python3 run.py setup
    python3 run.py build
    python3 run.py test-lexer
    python3 run.py test-parser
    python3 run.py test-ast
    python3 run.py clean
"""

import argparse
import os
import platform
import shutil
import subprocess
import sys
import time
import datetime
import threading
import tempfile
import filecmp
from termcolor import colored, cprint
import urllib.request
from pathlib import Path


class Colors:
    """Termcolor wrapper"""
    def red(self, text):
        return colored(text, "red")

    def green(self, text):
        return colored(text, "green")

    def yellow(self, text):
        return colored(text, "yellow")

    def blue(self, text):
        return colored(text, "blue")


class TyCBuilder:
    """Main builder class for TyC project."""

    def __init__(self):
        self.root_dir = Path(__file__).parent.absolute()
        self.external_dir = self.root_dir / "external"
        self.build_dir = self.root_dir / "build"
        self.report_dir = self.root_dir / "reports"
        self.venv_dir = self.root_dir / ".venv"

        self.antlr_version = "4.13.2"
        self.antlr_jar = f"antlr-{self.antlr_version}-complete.jar"
        self.antlr_url = f"https://www.antlr.org/download/{self.antlr_jar}"

        self.python_version = "3.12"

        self.colors = Colors()

        # Platform-specific paths
        if platform.system() == "Windows":
            self.venv_python3 = self.venv_dir / "Scripts" / "python.exe"
            self.venv_pip = self.venv_dir / "Scripts" / "pip.exe"
        else:
            self.venv_python3 = self.venv_dir / "bin" / "python"
            self.venv_pip = self.venv_dir / "bin" / "pip"

    def clear(self):
        os.system('cls')

    def run_command(self, cmd, cwd=None, check=True, capture_output=False):
        """Run a shell command."""
        try:
            if isinstance(cmd, str):
                result = subprocess.run(
                    cmd,
                    shell=True,
                    cwd=cwd or self.root_dir,
                    check=check,
                    capture_output=capture_output,
                    text=True,
                )
            else:
                result = subprocess.run(
                    cmd,
                    cwd=cwd or self.root_dir,
                    check=check,
                    capture_output=capture_output,
                    text=True,
                )
            return result
        except subprocess.CalledProcessError as e:
            if not capture_output:
                print(self.colors.red(f"Command failed: {e}"))
            if check:
                sys.exit(1)
            return e

    def command_exists(self, command):
        """Check if a command exists in PATH."""
        try:
            self.run_command([command, "--version"], capture_output=True, check=False)
            return True
        except:
            return False

    def find_python(self):
        """Find appropriate Python executable."""
        candidates = [f"python{self.python_version}", "python", "py"]

        for cmd in candidates:
            try:
                result = self.run_command(
                    [cmd, "--version"], capture_output=True, check=False
                )
                if result.returncode == 0 and self.python_version in result.stdout:
                    return cmd
            except:
                continue

        if platform.system() == "Windows":
            try:
                result = self.run_command(
                    [f"py", f"-{self.python_version}", "--version"],
                    capture_output=True,
                    check=False,
                )

                if result.returncode == 0:
                    return f"py -{self.python_version}"
            except:
                pass

        return None

    def show_help(self, **kwargs):
        """Show help information."""
        print(self.colors.blue("TyC Project - Available Commands:"))
        print()
        print(self.colors.green("Setup & Build:"))
        print(
            self.colors.yellow(
                "  python3 run.py setup     - Install dependencies and set up environment"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py build     - Compile ANTLR grammar files"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py check     - Check if required tools are installed"
            )
        )
        print()
        print(self.colors.green("Testing:"))
        print(
            self.colors.yellow(
                "  python3 run.py test-lexer  - Run lexer tests and generate reports"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py test-parser - Run parser tests and generate reports"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py test-ast    - Run AST generation tests and generate reports"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py test-checker - Run semantic checker tests (Assignment 3)"
            )
        )
        print()
        print(self.colors.green("Cleaning:"))
        print(
            self.colors.yellow(
                "  python3 run.py clean         - Clean build directories"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py clean-cache   - Clean Python cache files"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py clean-reports - Clean test reports directory"
            )
        )
        print(
            self.colors.yellow(
                "  python3 run.py clean-venv    - Remove virtual environment"
            )
        )
        print()
        print(self.colors.green("Environment:"))
        print(f"  Virtual environment: {self.venv_dir}")
        print(f"  Python version required: {self.python_version}")
        print(f"  ANTLR version: {self.antlr_version}")

    def check_dependencies(self, **kwargs):
        """Check if required dependencies are installed."""
        print(self.colors.blue("Checking required dependencies..."))
        print()

        # Check Java
        print(self.colors.yellow("Checking Java installation..."))
        if self.command_exists("java"):
            print(self.colors.green("✓ Java is installed"))
            java_ok = True
        else:
            print(self.colors.red("✗ Java is not installed"))
            java_ok = False

        print()

        # Check Python
        print(
            self.colors.yellow(f"Checking Python {self.python_version} installation...")
        )
        python_cmd = self.find_python()
        if python_cmd:
            print(
                self.colors.green(f"✓ Python {self.python_version} found: {python_cmd}")
            )
            python_ok = True
        else:
            print(
                self.colors.red(
                    f"✗ Python {self.python_version} is not installed or not found"
                )
            )
            python_ok = False

        print()
        print(self.colors.blue("Dependency check completed."))

        return java_ok and python_ok

    def setup_environment(self, **kwargs):
        """Set up the project environment."""
        print(self.colors.blue("Setting up project environment..."))

        self.external_dir.mkdir(exist_ok=True)

        if not self.check_dependencies():
            print(self.colors.red("Setup failed due to missing dependencies."))
            sys.exit(1)

        python_cmd = self.find_python()

        # Create virtual environment
        print(self.colors.yellow("Creating virtual environment..."))
        if not self.venv_dir.exists():
            self.run_command([python_cmd, "-m", "venv", str(self.venv_dir)])
            print(self.colors.green(f"Virtual environment created at {self.venv_dir}"))
        else:
            print(
                self.colors.blue(
                    f"Virtual environment already exists at {self.venv_dir}"
                )
            )

        # Download ANTLR
        print(self.colors.yellow(f"Downloading ANTLR version {self.antlr_version}..."))
        antlr_path = self.external_dir / self.antlr_jar
        if not antlr_path.exists():
            try:
                urllib.request.urlretrieve(self.antlr_url, antlr_path)
                print(self.colors.green(f"ANTLR downloaded to {antlr_path}"))
            except Exception as e:
                print(self.colors.red(f"Failed to download ANTLR: {e}"))
                sys.exit(1)
        else:
            print(self.colors.blue(f"ANTLR already exists at {antlr_path}"))

        # Upgrade pip
        print(self.colors.yellow("Upgrading pip in virtual environment..."))
        self.run_command([str(self.venv_pip), "-m", "pip", "install", "--upgrade", "pip"])

        # Install dependencies
        print(self.colors.yellow("Installing Python dependencies..."))
        self.run_command([str(self.venv_pip), "install", "-r", "requirements.txt"])

        print(self.colors.green("Setup completed!"))

    def watch(self, target, files, watch_kwargs, constant_check = True, force_close = False):
        init_thread = threading.Thread(target=target, kwargs=watch_kwargs)
        init_thread.start()
        init_thread.join()

        thread = threading.Thread(target=target, kwargs=watch_kwargs)
        if constant_check:
            while True:
                old_mod_times = [os.stat(file) for file in files]
                time.sleep(.25)
                curr_mod_times = [os.stat(file) for file in files]
                max_times = list(filter(lambda x: x, map(lambda x, y: x.st_mtime > y.st_mtime, curr_mod_times, old_mod_times)))

                if len(max_times) == 0:
                    continue

                if thread.is_alive():
                    thread.join()

                thread = threading.Thread(target=target, kwargs = watch_kwargs)
                self.clear()
                thread.start()

            return

        while True:
            if thread.is_alive():
                thread.join()

            old_mod_times = [os.stat(file) for file in files]
            time.sleep(.25)
            curr_mod_times = [os.stat(file) for file in files]
            max_times = list(filter(lambda x: x, map(lambda x, y: x.st_mtime > y.st_mtime, curr_mod_times, old_mod_times)))

            if len(max_times) == 0:
                continue

            thread = threading.Thread(target=target, kwargs = watch_kwargs)
            self.clear()
            thread.start()

    def build_grammar(self, watch = False, check = True, **kwargs):
        """Build ANTLR grammar files."""
        if self.build_dir.exists():
            shutil.rmtree(self.build_dir)

        antlr_path = self.external_dir / self.antlr_jar
        if check and not antlr_path.exists():
            print(self.colors.red("ANTLR jar not found. Please run 'setup' first."))
            sys.exit(1)

        self.build_dir.mkdir(exist_ok=True)

        grammar_files = list((self.root_dir / "src" / "grammar").glob("*.g4"))
        if check and not grammar_files:
            print(self.colors.red("No grammar files found in src/grammar/"))
            sys.exit(1)

        if check:
            print(self.colors.yellow("Compiling ANTLR grammar files..." + ("\n\tand watching..." if watch else "")))

        if not watch:
            cmd = [
                "java",
                "-jar",
                str(antlr_path),
                "-Dlanguage=Python3",
                "-visitor",
                "-no-listener",
                "-o",
                str(self.build_dir),
            ] + [str(f) for f in grammar_files]

            self.run_command(cmd)

            # Create __init__.py
            (self.build_dir / "__init__.py").touch()

            # Submissions Folder
            sub1_dir = self.root_dir / "submissions" / "ass_1"
            if not sub1_dir.exists():
                sub1_dir.mkdir(parents = True, exist_ok=True)

            sub2_dir = self.root_dir / "submissions" / "ass_2"
            if not sub2_dir.exists():
                sub2_dir.mkdir(parents = True, exist_ok=True)

            shutil.copytree(self.build_dir, sub1_dir, dirs_exist_ok = True)
            shutil.copy2(grammar_files[0], sub1_dir)

            shutil.copytree(self.build_dir, sub2_dir, dirs_exist_ok = True)
            shutil.copy2(grammar_files[0], sub2_dir)

            # Copy Python files
            lexererr_src = self.root_dir / "src" / "grammar" / "lexererr.py"
            lexererr_dst = self.build_dir / "lexererr.py"
            if lexererr_src.exists():
                shutil.copy2(lexererr_src, lexererr_dst)

            curr_time = datetime.datetime

            print(self.colors.green("ANTLR grammar files compiled to build/ at " + str(curr_time.now())))

            return

        watch_kwargs = {"watch" : False, "check": False}
        self.watch(target=self.build_grammar, files=grammar_files, watch_kwargs = watch_kwargs)

    def clean_cache(self, **kwargs):
        """Clean Python cache files."""
        print(self.colors.yellow("Cleaning Python cache files..."))
        for pattern in ["**/__pycache__", "**/*.pyc", "**/.pytest_cache"]:
            for path in self.root_dir.glob(pattern):
                if path.is_dir():
                    shutil.rmtree(path, ignore_errors=True)
                else:
                    path.unlink(missing_ok=True)
        print(self.colors.green("Python cache files cleaned."))

    def clean_reports(self, **kwargs):
        """Clean reports directory."""
        print(self.colors.yellow("Cleaning reports directory..."))
        if self.report_dir.exists():
            shutil.rmtree(self.report_dir)
        print(self.colors.green("Reports directory cleaned."))

    def clean_venv(self, **kwargs):
        """Clean virtual environment."""
        print(self.colors.yellow("Cleaning virtual environment..."))
        if self.venv_dir.exists():
            shutil.rmtree(self.venv_dir)
        print(self.colors.green("Virtual environment cleaned."))

    def clean_all(self, **kwargs):
        """Clean build and external directories."""
        print(self.colors.yellow("Cleaning build directories..."))
        if self.build_dir.exists():
            shutil.rmtree(self.build_dir)
        print(self.colors.green("Cleaned build directories."))
        self.clean_cache()

    def test_lexer(self, watch = False, check = True, **kwargs):
        """Run lexer tests."""
        grammar_files = list((self.root_dir / "src" / "grammar").glob("*.g4"))
        if not watch: 
            if check and not grammar_files:
                print(self.colors.red("No grammar files found in src/grammar/"))
                sys.exit(1)

            self.build_grammar()

            lexer_report_dir = self.report_dir / "lexer"
            #if check and lexer_report_dir.exists():
                #shutil.rmtree(lexer_report_dir)

            if not lexer_report_dir.exists():
                self.report_dir.mkdir(exist_ok=True)

            env = os.environ.copy()
            env["PYTHONPATH"] = str(self.root_dir)
            print(self.colors.yellow("Running lexer tests..." + ("\n\twatching..." if watch else "")))


            curr_time = datetime.datetime
            curr_time = str(curr_time.now().strftime('%Y-%m-%d %H-%M-%S'))

            test_dir = str(self.root_dir / "tests" / "test_lexer.py")

            self.run_command(
                [
                    str(self.venv_python3),
                    "-m",
                    "pytest",
                    test_dir,
                    f"--html={lexer_report_dir}/{curr_time}.html",
                    "--timeout=3",
                    "--self-contained-html",
                ],
                check=False,
            )

            print(self.colors.green(f"Lexer tests completed. Reports at {lexer_report_dir}/{curr_time}.html"))
            self.clean_cache()

            # Submissions Folder
            sub1_dir = self.root_dir / "submissions" / "ass_1"
            if not sub1_dir.exists():
                sub1_dir.mkdir(parents = True, exist_ok=True)

            shutil.copy2(test_dir, sub1_dir)

            return

        watch_kwargs = {"watch": False, "check": False}
        watch_files = ['tests\\test_lexer.py']
        watch_files.extend(grammar_files)

        self.watch(target = self.test_lexer, files = watch_files, watch_kwargs = watch_kwargs)

    def test_parser(self, check = True, watch = False, rebuild_grammar = True, **kwargs):
        """Run parser tests."""
        grammar_files = list((self.root_dir / "src" / "grammar").glob("*.g4"))

        if not watch:
            if check and not grammar_files:
                print(self.colors.red("No grammar files found in src/grammar/"))
                sys.exit(1)

            if rebuild_grammar:
                self.build_grammar()

            print(self.colors.yellow("Running parser tests..."))
            parser_report_dir = self.report_dir / "parser"

            env = os.environ.copy()
            env["PYTHONPATH"] = str(self.root_dir)

            curr_time = datetime.datetime
            curr_time = str(curr_time.now().strftime('%Y-%m-%d %H-%M-%S'))

            test_dir = str(self.root_dir / "tests" / "test_parser.py")

            self.run_command(
                [
                    str(self.venv_python3),
                    "-m",
                    "pytest",
                    test_dir,
                    f"--html={parser_report_dir}\\test_parser_{curr_time}.html",
                    "--timeout=5",
                    "--self-contained-html",
                ],
                check=False,
            )

            print(
                self.colors.green(
                    f"Parser tests completed. Reports at {parser_report_dir}\\test_parser_{curr_time}.html"
                )
            )
            self.clean_cache()

            # Submissions Folder
            sub1_dir = self.root_dir / "submissions" / "ass_1"
            if not sub1_dir.exists():
                sub1_dir.mkdir(parents = True, exist_ok=True)

            shutil.copy2(test_dir, sub1_dir)

            return

        watch_kwargs = {"watch": False, "check": False}
        watch_files = ["tests\\test_parser.py"]
        watch_files.extend(grammar_files)

        self.watch(target = self.test_parser, files = watch_files, watch_kwargs = watch_kwargs)

    def test_ast(self, watch = False, **kwargs):
        """Run AST generation tests."""
        if not watch:
            self.build_grammar()

            print(self.colors.yellow("Running AST generation tests..."))
            ast_report_dir = self.report_dir / "ast"

            env = os.environ.copy()
            env["PYTHONPATH"] = str(self.root_dir)

            curr_time = datetime.datetime
            curr_time = str(curr_time.now().strftime('%Y-%m-%d %H-%M-%S'))

            test_dir = str(self.root_dir / "tests" / "test_ast_gen.py")

            self.run_command(
                [
                    str(self.venv_python3),
                    "-m",
                    "pytest",
                    test_dir,
                    f"--html={ast_report_dir}/test_ast_{curr_time}.html",
                    "--timeout=5",
                    "--self-contained-html",
                    "-vv",
                ],
                check=False,
            )

            print(
                self.colors.green(
                    f"AST generation tests completed. Reports at {ast_report_dir}/test_ast_{curr_time}.html"
                )
            )
            self.clean_cache()

            # Submissions Folder
            sub2_dir = self.root_dir / "submissions" / "ass_2"
            if not sub2_dir.exists():
                sub2_dir.mkdir(parents = True, exist_ok=True)

            shutil.copy2(test_dir, sub2_dir)

            return

        watch_files = [self.root_dir / "src" / "grammar" / "TyC.g4", self.root_dir / "src" / "astgen" / "ast_generation.py", 
                       self.root_dir / "tests" / "test_ast_gen.py"]

        watch_kwargs = {'watch': False}
        self.watch(target = self.test_ast, files = watch_files, watch_kwargs = watch_kwargs, constant_check = False, force_close = True)

    def test_checker(self, watch = False, **kwargs):
        """Run static semantic checker tests (Assignment 3)."""
        if not watch:
            if not self.build_dir.exists():
                print(
                    self.colors.yellow("Build directory not found. Running build first...")
                )
                self.build_grammar()

            print(self.colors.yellow("Running semantic checker tests..."))
            checker_report_dir = self.report_dir / "checker"
            if not checker_report_dir.exists():
                self.report_dir.mkdir(exist_ok=True)

            env = os.environ.copy()
            env["PYTHONPATH"] = str(self.root_dir)

            curr_time = datetime.datetime
            curr_time = str(curr_time.now().strftime('%Y-%m-%d %H-%M-%S'))

            self.run_command(
                [
                    str(self.venv_python3),
                    "-m",
                    "pytest",
                    "tests/test_checker.py",
                    f"--html={checker_report_dir}/{curr_time}.html",
                    "--timeout=10",
                    "--self-contained-html",
                    "-vv",
                    "-l",
                ],
                check=False,
            )

            print(
                self.colors.green(
                    f"Checker tests completed. Reports at {checker_report_dir}/index.html"
                )
            )
            self.clean_cache()
            # test_dir = str(self.root_dir / "tests" / "test_checker.py")

            # Submissions Folder
            # sub3_dir = self.root_dir / "submissions" / "ass_3"
            # if not sub3_dir.exists():
            #     sub3_dir.mkdir(parents = True, exist_ok=True)
            #
            # shutil.copy3(test_dir, sub2_dir)
            return

        watch_files = [self.root_dir / "src" / "grammar" / "TyC.g4", 
                       self.root_dir / "src" / "semantics" / "static_checker.py", 
                       self.root_dir / "tests" / "test_checker.py"]

        watch_kwargs = {'watch': False}
        self.watch(target = self.test_checker, files = watch_files, watch_kwargs = watch_kwargs, constant_check = False, force_close = True)

    def test_gui(self, watch = False, ui = False, **kwargs):
        if not watch:
            print(self.colors.yellow("Running Test with GUI..."))
            grammar_file = open(self.root_dir / "src" / "grammar" / "TyC.g4")
            java_grammar_file = open(self.root_dir / "java_tester" / "TyC.g4", "w")

            java_grammar_file.write(grammar_file.readline())

            for i in range(27):
                grammar_file.readline()

            skipping = True
            while line := grammar_file.readline():
                if 'TODO' in line:
                    skipping = False

                if skipping:
                    continue

                java_grammar_file.write(line)

            grammar_file.close()
            java_grammar_file.close()

            antlr_path = self.external_dir / self.antlr_jar
            java_tester_path = self.root_dir / "java_tester"

            self.run_command([
                "java",
                "-cp",
                antlr_path,
                "org.antlr.v4.Tool",
                "java_tester\\TyC.g4",
            ])

            self.run_command([
                "javac",
                "-cp",
                antlr_path,
                "java_tester\\*.java"
            ])

            self.run_command([
                "java",
                "-cp",
                f"{java_tester_path};{antlr_path}",
                "org.antlr.v4.gui.TestRig",
                "TyC",
                "program",
                "java_tester\\test.tyc",
                "-gui",
            ])

            return

        watch_files = [self.root_dir / "java_tester" / "test.tyc", self.root_dir / "src" / "grammar" / "TyC.g4"]

        watch_kwargs = {'watch': False}
        self.watch(target = self.test_gui, files = watch_files, watch_kwargs = watch_kwargs, constant_check = False, force_close = True)

    def test_all(self, watch = False, ui = False, parts = ['1', '2', '3', '4'], **kwargs):
        self.clear()
        if parts == None:
            parts = ['1', '2', '3', '4']

        if not watch:
            if '1' in parts:
                self.test_lexer()
                self.test_parser(rebuild_grammar = False)

            if '2' in parts:
                self.test_ast()

            return

        grammar_files = list((self.root_dir / "src" / "grammar").glob("*.g4"))
        if not grammar_files:
            print(self.colors.red("No grammar files found in src/grammar/"))
            sys.exit(1)

        watch_files = []

        if '1' in parts:
            watch_files.extend(grammar_files)
            watch_files.append("tests/test_lexer.py")
            watch_files.append("tests/test_parser.py")

        watch_kwargs = {'watch': False, 'parts': parts}

        self.watch(target = self.test_all, files = watch_files, watch_kwargs = watch_kwargs)

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="TyC Project Build Script",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "command",
        nargs="?",
        default="help",
        choices=[
            "help",
            "check",
            "setup",
            "build",
            "clean",
            "clean-cache",
            "clean-reports",
            "clean-venv",
            "test-lexer",
            "test-parser",
            "test-ast",
            "test-checker",
            "test-gui",
            "test-all"
        ],
        help="Command to execute",
    )

    parser.add_argument(
            "--watch",
            action="store_true"
            )

    parser.add_argument(
            "--parts",
            nargs='*'
            )
    
    args = parser.parse_args()

    builder = TyCBuilder()

    commands = {
        "help": builder.show_help,
        "check": builder.check_dependencies,
        "setup": builder.setup_environment,
        "build": builder.build_grammar,
        "clean": builder.clean_all,
        "clean-cache": builder.clean_cache,
        "clean-reports": builder.clean_reports,
        "clean-venv": builder.clean_venv,
        "test-lexer": builder.test_lexer,
        "test-parser": builder.test_parser,
        "test-ast": builder.test_ast,
        "test-checker": builder.test_checker,
        "test-gui": builder.test_gui,
        "test-all": builder.test_all
    }

    kwargs = {
            'watch': args.watch,
            'parts': args.parts
    }

    if args.command in commands:
        commands[args.command](**kwargs)
    else:
        print(f"Unknown command: {args.command}")
        builder.show_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
