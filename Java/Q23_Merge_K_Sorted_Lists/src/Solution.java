// Suboptimal solution, but it does work

class Solution {
    //    Checks for all null values
    private boolean checkForAllNull(ListNode[] lists){
        if (lists == null) {
            return true;
        }
        for (Object element : lists) {
            if (element != null) {
                return false;
            }
        }
        return true;
    }
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode final_head = null;
        ListNode f_ptr = null;

//        null check
        if (lists == null || checkForAllNull(lists)){
            return null;
        }

//        Find for minimum value
        int mink = 0;
        int minval = Integer.MAX_VALUE;
        for (int k = 0; k < lists.length; k++){
            if (lists[k] != null) {
                if (lists[k].val < minval){
                    mink = k;
                    minval = lists[k].val;
                }
            }
        }
        final_head = lists[mink];
        f_ptr = final_head;
        lists[mink] = lists[mink].next;

//        iterate through until ptr list is all null pointers
        while (!checkForAllNull(lists)){
            mink = 0;
            minval = Integer.MAX_VALUE;
//            Find next minimum value
            for (int k = 0; k < lists.length; k++){
                if (lists[k] != null) {
                    if (lists[k].val < minval){
                        mink = k;
                        minval = lists[k].val;
                    }
                }
            }
//            Splice in new value
            f_ptr.next = lists[mink];
            f_ptr = f_ptr.next;
            lists[mink] = lists[mink].next;
        }

        return final_head;
    }
}