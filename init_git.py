#!/usr/bin/env python
import subprocess
import os

def run_command(command):
    """Run a shell command and print output"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    return result.returncode == 0

def main():
    """Initialize Git repository and perform initial commit"""
    # Initialize repository
    if not run_command("git init"):
        return
    
    # Add files
    if not run_command("git add ."):
        return
    
    # Initial commit
    if not run_command('git commit -m "Initial commit: CrewAI Procurement Agent"'):
        return
    
    print("\nGit repository initialized successfully!")
    print("\nNext steps:")
    print("1. Create a repository on GitHub, GitLab, or other Git hosting service")
    print("2. Run the following command to add your remote origin:")
    print("   git remote add origin <your-repository-url>")
    print("3. Push your code with:")
    print("   git push -u origin main")  # or master depending on your default branch name

if __name__ == "__main__":
    main()
    