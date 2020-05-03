#include<iostream>
#include<unistd.h>
#include<stdio.h>
#include<fcntl.h>

using namespace std;
int main()
{
	int fds[2];
	if(pipe(fds) == -1)
	{

		perror("pipe error");
		exit(EXIT_FAILURE);
	}
	pid_t pid;
	pid = fork();
	if(pid == -1)
	{
		perror("fork error");
		exit(EXIT_FAILURE);
	}
	if(pid == 0)
	{
		close(fds[0]);
		sleep(10);
		write(fds[1], "hello", 5);
		exit(EXIT_SUCCESS);

	}
	close(fds[1]);
	char buf[10] = {0};
	read(fds[0], buf, 10);
	cout << "receive data " << buf << endl;
	return 0;
}
