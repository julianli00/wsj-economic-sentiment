# Teamwork Contract

## 1. Team Members and Roles
Each team member has been assigned specific responsibilities based on their strengths and expertise to ensure the project’s success.

### Yuchen Li (Group leader. Strong coding skills, expertise in algorithm optimization and efficient data handling)
- Extracting data from target websites and designing storage structures  
- Maintaining the GitHub repository and facilitating team collaboration  
- Reviewing and optimizing code for efficiency

- ### Yiyang Du (Proficient in Python and web scraping, strong logical thinking, excellent coding skills)
- Developing and optimizing web scraping scripts  
- Managing the GitHub repository and ensuring code quality  
- Conducting code reviews and verifying data processing accuracy  

### Tiffany (Careful, patient, excellent writing and documentation skills)
- Text annotation and data organization  
- Assisting in project design and providing insights for text analysis  
- Supporting documentation writing  

### Miaolin Zhang (Strong text processing skills, logical thinker, meticulous and detail-oriented)
- Designing and executing the annotation scheme  
- Initial project framework and planning  
- Writing and organizing documentation (team contract, project proposal)  

All team members will collaborate and support each other beyond their primary tasks to ensure the project progresses smoothly.

## 2. Repository Management (Repo Setup)
### Repository Location
The team will create a private repository on UBC GitHub. All members will have write access, and instructors will have read access.

### Branch Management
Each team member will work on an individual branch and is not allowed to push directly to the master branch. All contributions must go through Pull Requests (PRs) and be reviewed by at least one team member before merging.

### Folder Structure
```
wsj-corpus-annotation/        # Project root directory
│── docs/            # Documentation files
│   ├── proposal.md             # Project proposal
│   ├── teamwork_concept.md     # Teamwork concept explanation
│   ├── proof_of_concept.md     # Proof of concept documentation
│── data/            # Data storage
│   ├── wsj_econ_articles_2023-01-01_2024-12-31.csv     # Main dataset with annotations
│── src/             # Source code
│   ├── wsj_scraper.ipynb          # Main script for processing and analyzing data
│   ├── wsj_scraper_test.py      # Unit tests for data processing scripts
│── environment.yml      # Conda environment file
│── LICENSE           # License file
│── README.md         # Project documentation
```

### README File
The repository should contain a clear README file explaining its structure, code usage, and data storage format.

## 3. Meeting Schedule
The team will hold three meetings per week:
- **One online meeting** to update progress and assign new tasks.
- **Two in-person meetings** to discuss issues encountered and review the work.

All meetings will be recorded and stored in the `docs/` folder within the repository. The Scrum Leader of the week will be responsible for maintaining and uploading these records.

Team members are expected to attend meetings on time. If someone is unable to attend, they must notify the team in advance and provide a written progress update.

## 4. Task Allocation & Workflow
### Work Schedule & Deadlines
All tasks must be completed and submitted by **Friday at 11:00 PM** each week. If any issues arise that prevent completion, the team will discuss and resolve them in a dedicated problem-solving session on **Saturday at 11:00 AM**.

### Task Responsibilities
- **Miaolin Zhang and Tiffany** will design and execute the annotation scheme, ensuring consistency and high-quality annotation. They will also draft documentation such as the project proposal and annotation guidelines.
- **Yiyang Du and Yuchen Li** will handle data extraction, writing and debugging web scrapers, managing data storage formats, and reviewing code to maintain efficiency.
- **All team members** will contribute to ensuring the clarity and quality of the project’s deliverables, providing support where needed.

## 5. Scrum Leader Rotation
Each week, a different team member will serve as the Scrum Leader, responsible for:
- Organizing and leading meetings.
- Tracking project progress and ensuring that tasks are completed on time.
- Assigning clear responsibilities to team members.
- Maintaining and uploading meeting records.

### Rotation Schedule
- **Week 1:** Yuchen Li  
- **Week 2:** Yiyang Du  
- **Week 3:** Yiyang Du  
- **Week 4:** Miaolin Zhang  

## 6. Code Review & Quality Standards
Before merging any code into the master branch, team members must:
1. Work on a personal branch and submit changes via a Pull Request.
2. Have at least one team member review and approve the code.

### Quality Standards
- Follow **PEP8** guidelines for Python code formatting.
- Provide clear comments and documentation for important functions and data processing steps.
- Implement error handling in web scrapers to prevent failures due to format changes.
- Test all code locally before submitting PRs to ensure there are no errors.

## 7. Communication Methods
- **Slack:** The primary tool for quick updates and problem-solving discussions.
- **GitHub Issues:** Used for tracking task progress, reporting bugs, and documenting challenges.
- **Email:** Reserved for formal communications, such as discussions with instructors or submitting important project files.

## 8. Team Availability & Leave Policy
If a team member cannot work due to exams, personal commitments, or other reasons, they must notify the team **at least 24 hours in advance** via Slack and submit a written progress report.

Absences close to critical deadlines (e.g., sprint submission dates) are discouraged. If a member is frequently unavailable or unable to complete tasks, the team will discuss possible task reallocation with the instructor.

## 9. Team Conduct & Conflict Resolution
To ensure a productive and respectful working environment, all team members agree to:
- **Meet deadlines:** Repeated failure to complete tasks on time will lead to a discussion on workload adjustment.
- **Take responsibility:** Everyone must be accountable for their assigned tasks and communicate any difficulties in advance.
- **Distribute work fairly:** If any imbalance is noticed, it should be addressed in team meetings.
- **Respect each other:** Disagreements should be handled professionally to avoid conflicts.

## 10. Code Style & Best Practices
To maintain consistency, the team will adhere to the following guidelines:
- Follow **PEP8** coding standards and use tools like **black** or **flake8** for automatic formatting.
- Use meaningful filenames instead of generic ones like `test1.py`.
- Implement logging in critical parts of the code for debugging and tracking progress.

## 11. Self-Evaluation
Each team member has evaluated their skills in four key areas, which will inform role assignments:

| Team Member    | Communication | Creativity | Analytical | Integration |
|---------------|--------------|-----------|------------|------------|
| Miaolin Zhang | 5/5          | 5/5       | 4/5        | 4/5        |
| Tiffany       | 5/5          | 5/5       | 4/5        | 4/5        |
| Yiyang Du     | 4/5          | 4/5       | 5/5        | 5/5        |
| Yuchen Li     | 4/5          | 4/5       | 5/5        | 5/5        |

Based on these strengths, team members have been assigned roles that align with their expertise.

## 12. Contract Modifications
If any changes are needed, the entire team must agree before modifying this contract.

Any modifications must be documented, including the reason for the change, and stored in the `docs/` folder.
