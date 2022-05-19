class app6 {
    public static void main(String[] args) {
        String[] fname = new String[]{"bob"  , "joe" , "john" , "bob"};
        String[] lname = new String[]{"mccaffery" , "biden" , "doe" , "cat"}  ;
        String[] res = qa(fname,lname);
        for(int x  = 0;x < res.length;x++){
            System.out.println(res[x]);
        }
        
    }

    // ["larry", "bob"] ["tan", "tom"]
    // ["larry tan", "bob tom"]

    public static String[] qa(String[] fname , String[] lname){
        String[] funame = new String[fname.length]; 
        for(int i = 0;i < lname.length;i++){
            funame[i] = fname[i] + " " + lname[i];
        }
        
        return funame;
    }
}
