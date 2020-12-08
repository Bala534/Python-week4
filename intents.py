name = ''
plantname = ''
plantinfo = ''


def get_intent(data):
    global name, plantname, plantinfo
    m=data['message'].lower()

    if data['key']=="name":
        name=m
        return "next"
    
    if any(x in m for x in ["mango","tomato","greengram","cotton","hibiscus"]):
        plantname=m
        return "plantname"
    
    if any(x in m for x in ["soil","water","days","how"]):
        plantinfo=m
        return "plantinfo"
    
    if "thank" in m:
        return "end"


def handle(data):
    global name, plantname, plantinfo
    from flask import render_template
    intent = get_intent(data)

    if intent == 'plantname':
        return render_template('messages/aboutplant1.html', question={'key':'request','text':'Please Enter the details you want to know.'},options={'tasks':[
        {'key':'soil','description':'to know what soil to use'},
        {'key':'water','description':'for how much water rquired'},
        {'key':'days','description':'to know days rquired to get a fruit/flower/vegetable'},
        {'key':'how','description':'to know full procedure to plant'}
        
    ] })

    elif intent == 'next':
        return render_template('messages/greet.html',name=name, question={'key':'request','text':'Enter the plant name you want to grow Ex: Mango, Cotton, Tomato, Greengram, Hibiscus, etc., '})
    
    elif intent == 'plantinfo':
        from data.info import bot
        return render_template('messages/aboutplant2.html',plantname=plantname,plantinfo=plantinfo,data=bot ,question={'key':'request'})
    
    elif intent == 'end':
        return render_template('messages/botend.html',question={'key':'request'})
    
    else:
        return render_template('messages/echo.html', question={'key':'request'})