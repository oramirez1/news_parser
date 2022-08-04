# Contribution Process

1. Select or Create an Issue or Select and Issue from the [Issues site](https://github.com/oramirez1/news_parser/issues).
2. Update/Edit the issue and add yourself to the Assignee.
3. Clone the project 

    ```
    $ git clone git@github.com:oramirez1/news_parser.git
    ```
   
4. Create a branch with the issue number (i.e. The issue is 37, the branch is issue_37)

    ```
     $ cd news_parser
     $ git checkout -b develop origin/develop
     $ git checkout -b <issue_number>
    ```

5. commit the branch to your repo

    ```
     $ git commit
     $ git push --set-upstream origin <issue_number>
    ```

6. Now you're ready to create a pull request to the develop branch.
