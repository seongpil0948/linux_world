
# for i in {1..5}; do ssh-copy-id root@192.168.100.$i; done
# for i in {2..4}; do ssh-copy-id -p "222$i" root@127.0.0.1 ; done
for i in {2..4};
do
    ssh-keygen -R [127.0.0.1]:222$i;
    # ssh-copy-id -p "222$i" root@127.0.0.1;
done