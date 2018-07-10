
#对于不下降序列a，n为序列a元素的个数，key为关键字：
#取最小的i，向下取整
int binary_search1(int[] array,int len,int key){
    int low=0,mid=0,high=len-1
    while(low<high){
        mid = low + (high-low)>>1;
        if(array[mid]<key){
            low = mid+1;
        }else{
            high = mid;
        }
    }
    if(array[hign]==key) return high;
    return -1;
}
#取最大的i，向下取整
int binary_search2(int[] array,int len,int key){
    int low=0,mid=0,high=len-1;
    while(low < high){
        mid = low + (high-low)>>1;
        if(array[mid] > key){
            high = mid;
        }else{
            low =mid+1;
        }
    }
}
    