class Solution {
public:
    int numUniqueEmails(vector<string>& emails) {
        
        vector <string> processed_emails;
        for (int i=0; i< emails.size(); i++){
            string email = emails[i];
            int pos_at = email.find("@");
            string local = email.substr(0,pos_at);
            string domain = email.substr(pos_at+1);
            //std::cout<< "split local: "<<local<<"\n";
           
            int pop_plus = local.find("+");
            if (pop_plus != -1){
                local = local.substr(0,pop_plus);
            }
            //std::cout<< "after + local:"<<local<<"\n";
            int pos_dot=local.find(".");;
            while(pos_dot != -1){
                local = local.substr(0,pos_dot) + local.substr(pos_dot+1);
                //std::cout<< "after . local: "<<local<<"\n";
                pos_dot = local.find(".");
                //std::cout<< "pos_dot: "<<pos_dot<<"\n";
            }
           //std::cout<< "domain: "<<domain<<"\n";
            email = local + domain;
            //std::cout<< "email"<< email<<"\n";
            if (std::find(processed_emails.begin(), processed_emails.end(), email)== processed_emails.end()){
                processed_emails.push_back(email);
            }
            
        }
        return processed_emails.size();
        
    }
};