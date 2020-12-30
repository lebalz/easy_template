# Programming Examn 1

Name: {{=first_name}} {{=last_name}}

Grade: {{=evaluation.grade}}

## Question 1

Points: {{=evaluation.question1.achieved}} / {{=evaluation.question1.max}}

{{%py% hello_world.py}}

## Question 2

Points: {{=evaluation.question2.achieved}} / {{=evaluation.question2.max}}

{{%py%=question2}}
