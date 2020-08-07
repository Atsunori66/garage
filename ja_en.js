javascript:(
    function(){
        a='ja-jp';b='en-us';c='ja_jp';d='en_us';
        if(document.location.href.indexOf(a)>=0){
            location.href=document.location.href.replace(a,b);
        }else if(document.location.href.indexOf(b)>=0){
            location.href=document.location.href.replace(b,a);
        }else if(document.location.href.indexOf(c)>=0){
            location.href=document.location.href.replace(c,d);
        }else{location.href=document.location.href.replace(d,c);
        }
    }
)(location.href);


javascript:(function(){a='ja-jp';b='en-us';c='ja_jp';d='en_us';if(document.location.href.indexOf(a)>=0){location.href=document.location.href.replace(a,b);}else if(document.location.href.indexOf(b)>=0){location.href=document.location.href.replace(b,a);}else if(document.location.href.indexOf(c)>=0){location.href=document.location.href.replace(c,d);}else{location.href=document.location.href.replace(d,c);}})(location.href);