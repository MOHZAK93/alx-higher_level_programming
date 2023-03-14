#include <stdio.h>
/* If the appraisal score is a - c, the person qualifies for the
 *appraisal, else the person has to get a better score!
 *If the person's appraisal is a , the person gets ((salary * 0.2) + 1000)
 *If the appraisal score is b, the person gets ((salary * 0.2) + 700)
 *If the appraisal is c, the person gets ((salary * 0.2) + 500)
 */
int main()
{
	int appraisal_score, salary;
	printf("Enter your appraisal score:\n");
	appraisal_score = getchar();
	if (appraisal_score <= 'c')
	{
		salary = getchar();
		printf("Congratulations! You deserve more. What is your current salary?\n");
		/*scanf("%d", &salary);*/

		if (appraisal_score == 'a')
			salary = ((salary * 0.2) + 1000 + salary);
		else if (appraisal_score == 'b')
			salary = ((salary * 0.2) + 700 + salary);
		else
			salary = ((salary * 0.2) + 500 + salary);
		printf("New salary is %d\n", salary);
	}
	else
	{
		printf("Perform better next year! :)\n");
	}
	return (0);
}

