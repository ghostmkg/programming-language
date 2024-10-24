class Solution {
    public int sumOfLastN_Nodes(Node head, int n) {
        int c =0;int resf = 0;
        Node temp1 = head;
        Node temp2 = head;
        while(temp1 != null){
            c++;
            if(temp1.next !=null) temp1=temp1.next;
            else{break;}
        }
        while(temp2!=null){
            if(c==n) resf += temp2.data;
            else c--;
            
            if(temp2.next !=null) temp2=temp2.next;
            else{break;}
        }
        return resf;
    }
}
