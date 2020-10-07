javascript:(
    function(){
        a='ja-jp';b='en-us';
        c='ja_jp';d='en_us';
        e=document.location.pathname.substr(1,5); // MS docs 多言語用
        if(document.location.href.indexOf(a)>=0){
            location.href=document.location.href.replace(a,b);
        }else if(document.location.href.indexOf(b)>=0){
            location.href=document.location.href.replace(b,a);
        }else if(document.location.href.indexOf(c)>=0){
            location.href=document.location.href.replace(c,d);
        }else if(document.location.href.indexOf(d)>=0){
            location.href=document.location.href.replace(d,c);
        }else if(e!='en-us'){
            location.href=document.location.href.replace(e,b);
        }
    }
)(location.href);

javascript:(function(){a='ja-jp';b='en-us';c='ja_jp';d='en_us';e=document.location.pathname.substr(1,5);if(document.location.href.indexOf(a)>=0){location.href=document.location.href.replace(a,b);}else if(document.location.href.indexOf(b)>=0){location.href=document.location.href.replace(b,a);}else if(document.location.href.indexOf(c)>=0){location.href=document.location.href.replace(c,d);}else if(document.location.href.indexOf(d)>=0){location.href=document.location.href.replace(d,c);}else if(e!='en-us'){location.href=document.location.href.replace(e,b);}})(location.href);