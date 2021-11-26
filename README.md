# CSCGenerationHomeExcercise
Home excercise for QA position


I was not able to commit all the files related to this project due to some access issue so I uploaded the py file directly and commited the changes. You can copy the "gitHubRepositoryModule.py" file into your projects where selenium is already imported and can execute.

I have committed the screen recording file also for the scripts execution.

Below is my console out put after my excution results:

/Users/SGLG/eclipse-workspace/CSCGeneration/gitHubRepository/gitHubRepositoryModule.py:13: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome(executable_path="/Users/SGLG/Documents/chromedriver")
=================================================
Number of repositories found:   1 repository result
One repository found:
True
==================================================
Name of the repository found:  mvoloskov/decider
Repository Name found:
True
======== FIRST 300 CHARACTERS OF README============
🤔 Decider
Apply CSS to React components conditionally, like a boss.
className={ decide(styles, {
    header: true,
    mobile: props.isMobile,
    narrow: parseInt(props.width) < 400,
    hidden: (props.hidden !== "false" && Boolean(props.hidden)),
    fixed: parseInt(props.width) >= 400 || !props.i
