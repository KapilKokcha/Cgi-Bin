- hosts: all
  tasks:
     - copy:
          content: "this is data"
          dest: "/root/z.txt"
