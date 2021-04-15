echo '======================================  =를 이용해서 선언하고 $를 이용해서 사용'
test="abc"
num=100

echo "${test}"
echo "${num}"
echo '======================================# Array'

arr_test_num=(1 2 3 100 10000)
arr_test_string=("abc" "def" "ghi" "jkl")

arr_test_string+=('hihi')


echo "${arr_test_num[3]}"

echo "${arr_test_num[@]}"

for i in ${arr_test_string[@]}; do
	echo $i
done    

echo '====================================== # remove using /'
arr_test=("abc" "def" "defghi")
remove_element=("def")


arr_test=( "${arr_test[@]/$remove_element}" )

for i in ${arr_test[@]}; do
	echo $i
done

echo '========================= condition '
test_num=5

if [ "${test_num}" -eq 2 ]; then
	echo "number is 2"
elif [ "${test_num}" -eq 3 ]; then
	echo "number is 3"
else
	echo "number is not 2 or 3"
fi



# 1, 3, 5 세 번 실행

for i in {1..5..2}
do
   echo "Welcome $i times"
done