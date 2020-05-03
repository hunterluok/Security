#include<iostream>
#include<signal.h>
#include<sys/wait.h>
#include<sys/types.h>
#include<stdlib.h>

using namespace std;

#include<unistd.h>
#include<stdio.h>

int main()
{
	pid_t fpid;
//	int count = 0;
	int status;
	int retal;
	fpid = fork();
	if(fpid < 0)
	{
		cout << "failed to fork" << endl;
	}
	else if(fpid ==0)
	{
		cout << "iam child" << getpid() << endl;
		sleep(100);
		exit(EXIT_SUCCESS);
		//count++;
	}
	else
	{
		if(0==(waitpid(fpid,&status,WNOHANG)))
		{
			retal = kill(fpid, SIGKILL);
			if(retal)
			{
				puts("kill failed");
				perror("kill");
				waitpid(fpid, &status, 0);
			}
			else
			{
				cout << " killed " << endl;
			}
		}
		cout << "i am the parent " << getpid() << endl;
		cout << "fpid = " << fpid << endl;
//		count++;
	}
//	cout << "result " << count << endl;
	
	execl("/bin/pwd","sdas", NULL);

	return 0;
}
