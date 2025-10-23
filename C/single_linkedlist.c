
#include <stdio.h>
#include <stdlib.h>
struct list{
	int info;
	struct list *next;
	};struct list *start;
void insert_begin();
void insert_end();
void insert_middle();
void insert_after_data();
void delete_begin();
void delete_end();
void delete_middle();
void delete_data();

void main()
{
	struct list *node;
	char ch,e;
	node=(struct list*)malloc(sizeof(struct list));
	start=node;
	printf("Enter Data:\n");
	scanf("%d",&node->info);
	printf("Do you want to create more(Y/N)?");scanf("%c",&e);
	scanf("%c",&ch);
	while(ch!='n'&&ch!='N')
	{
		node->next=(struct list*)malloc(sizeof(struct list));
		node=node->next;
		printf("Enter Data:\n");
		scanf("%d",&node->info);
		printf("Do you want to create more(Y/N)?");scanf("%c",&e);
		scanf("%c",&ch);
		fflush(stdin);
	}
	node->next=NULL;
	printf("\n Linked List is:");
	struct list *temp;
	temp=(struct list*)malloc(sizeof(struct list));	
	temp=start;
	while(temp!=NULL)
	{
		printf("%d ",temp->info);
		temp=temp->next;
	}
	int s,s1;
	printf("Enter 1 for Insertion and 2  for Deletion\n");
	scanf("%d",&s);
	switch(s)
	{
		case 1:
		printf("Enter 1 to Insert at the beginning\n");
		printf("Enter 2 to Insert at the end\n");
		printf("Enter 3 to Insert at a given  position\n");
		printf("Enter 4 to Insert after a given data\n");
	        scanf("%d",&s1);
		switch(s1)
		{
		    case 1:
		    insert_begin();
		    break;
		      case 2:
		    insert_end();
		    break;
		      case 3:
		    insert_middle();
		    break;
		      case 4:
		    insert_after_data();
		    break;
		    default:
		    printf("Wrong Choice");
		   }
		   break;
		 case 2:
		printf("Enter 1 to delete from the beginning\n");
		printf("Enter 2 to delete from the end\n");
		printf("Enter 3 to delete from a given  position\n");
		printf("Enter 4 to delete  a given data\n");
		scanf("%d",&s1);
		switch(s1)
		{
		    case 1:
		    delete_begin();
		    break;
		      case 2:
		    delete_end();
		    break;
		      case 3:
		    delete_middle();
		    break;
		      case 4:
		    delete_data();
		    break;
		    default:
		    printf("Wrong Choice");
		   }
		   break;
		    default:
		    printf("Wrong Choice");
	}
	printf("\n Changed Linked List is:");
	temp=start;
	while(temp!=NULL)
	{
		printf("%d ",temp->info);
		temp=temp->next;
	}
}

void insert_begin()
{
	struct list *ptr;
	ptr=(struct list*)malloc(sizeof(struct list));		 
	printf("Enter element to be inserted\n");
	scanf("%d",&ptr->info);
	ptr->next=start;
	start=ptr;	    
}	    
		    
void insert_end()
{
	struct list *ptr,*t;
	ptr=(struct list*)malloc(sizeof(struct list));	
	t=(struct list*)malloc(sizeof(struct list));	
	printf("Enter element to be inserted\n");
	scanf("%d",&ptr->info);
	ptr->next=NULL;
	t=start;
	while(t->next!=NULL)
	{
		t=t->next;
	}
	t->next=ptr;
}
void insert_middle()
{
	struct list *ptr,*t;
	int pos;
	ptr=(struct list*)malloc(sizeof(struct list));		
	printf("Enter element to be inserted\n");
	scanf("%d",&ptr->info);	  
	printf("Enter the position of insertion\n");
	scanf("%d",&pos);
	t=start;
	for(int i=1;i<pos-1;i++)
	{
			t=t->next;
	}
	if(t==NULL)
	{
		printf("Position not found");
		return;
	}
	ptr->next=t->next;
	t->next=ptr;
}
void insert_after_data()
{
	struct list *node=start,*nw;
	nw=(struct list*)malloc(sizeof(struct list));
	int item;
	printf("Enter the data to insert\n");
	scanf("%d",&nw->info);
	printf("Enter the data after which new data will be inserted\n");
	scanf("%d",&item);
	while(node!=NULL && node->info!=item)
	{
		node=node->next;
	}
	if(node==NULL)
	{
		printf("Item not found");
		return;
	}
	nw->next=node->next;
	node->next=nw;
}

void   delete_begin()
{
	struct list *ptr;
	if(start==NULL)
	{
		printf("List is empty");
		return;
	}
	ptr=start;
	start=start->next;
	printf("Deleted element is %d",ptr->info);
	free(ptr);
}
void delete_end()
{
	struct list *ptr,*t;
	if(start==NULL)
	{
		printf("List is Empty");
		return;
	}
	ptr=start;
	while(ptr->next!=NULL)
	{
		t=ptr;
		ptr=ptr->next;
	}
	t->next=NULL;
	printf("Deleted element is %d",ptr->info);
	free(ptr);
}
void delete_middle()
{
	struct list *ptr,*t;
	int pos,i;
	printf("Enter the position for deletion\n");
	scanf("%d",&pos);
	if(start==NULL)
	{
		printf("List is Empty");
		return;
	}
	ptr=start;
	for(i=1;i<pos;i++)
	{
		t=ptr;
		ptr=ptr->next;
	}
	if(t==NULL)
	{
		printf("Position not found");
		return;
	}
	t->next=ptr->next;
	printf("Deleted element is %d",ptr->info);
	free(ptr);
	}
void delete_data()
{
	struct list *ptr,*temp;
	int item;
	printf("Enter the item to be deleted\n");	
	scanf("%d",&item);
	if(start==NULL)
	{
		printf("List is Empty");
		return;
	}
	ptr=start;
	while(ptr!=NULL && ptr->info!=item)
	{
	        temp=ptr;
		ptr=ptr->next;
	}
	temp->next=ptr->next;
	free(ptr);
}
	
