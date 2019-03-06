public:
    string toLowerCase(string str) {

        for (int i=0; i<str.size(); i++){
            int cdec = 'a'- str[i];
            if (cdec >= 7 && cdec <= 32){
                str[i] = str[i]+32;
            }
        }
        return str;
    }