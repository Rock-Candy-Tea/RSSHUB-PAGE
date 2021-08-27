
---
title: 'Flutter SingleChildScrollView 滚动页面'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=585'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 20:28:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=585'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我尝试使用 SingleChildScrollView 创建滚动页面但出现错误，我该如何解决问题？结果想要的是固定的appbar 和一个可滚动的表单。错误：RenderFlex 子项具有非零 flex 但传入的高度约束是无界的。错误似乎告诉我高度不够，但我对自己犯的错误感到沮丧。我设计的代码</p>
<pre><code class="copyable">import 'package:dailyreport/weatheritem.dart';
import 'package:scroll_snap_list/scroll_snap_list.dart';

class ReferenceDetail extends StatefulWidget &#123;
  @override
  _ReferenceDetailState createState() => _ReferenceDetailState();
&#125;

class _ReferenceDetailState extends State<ReferenceDetail> &#123;
  final _formKey = GlobalKey<FormState>();
  late Function slideAction;
  List<Widget> weatherData = [];
  ScrollController controller = ScrollController();
  bool closeTopContainer = false;
  double topContainer = 0;
  int _focusedIndex = 0;

  void _onItemFocus(int index) &#123;
    setState(() &#123;
      _focusedIndex = index;
    &#125;);
  &#125;

  void getPostData() &#123;
    List<dynamic> returnweather = WEATHERITEM; //get the weather data
    List<Widget> weatherlist = [];
    returnweather.forEach((post) &#123;
      weatherlist.add(
        Container(
          height: 200,
          width: 120,
          margin: const EdgeInsets.symmetric(horizontal: 15.0, vertical: 40.0),
          decoration: BoxDecoration(
              borderRadius: BorderRadius.all(Radius.circular(5.0)),
              color: Colors.white,
              boxShadow: [
                BoxShadow(color: Colors.black.withAlpha(100), blurRadius: 5.0),
              ]),
          child: Padding(
            padding:
                const EdgeInsets.symmetric(horizontal: 10.0, vertical: 10.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                Image.asset(
                  post["weather"],
                ),
                SizedBox(height: 5.0),
                Text(
                  post["weather_name"],
                  style: const TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                    color: Colors.grey,
                  ),
                ),
              ],
            ),
          ),
        ),
      );
    &#125;);
    setState(() &#123;
      weatherData = weatherlist;
    &#125;);
    SizedBox(height: 50.0);
  &#125;

  int selectedRadio = 0;

  @override
  void initState() &#123;
    super.initState();
    selectedRadio = 0;
    _onItemFocus(_focusedIndex);
    getPostData();
    controller.addListener(() &#123;
      double value = controller.offset / 119;
      setState(() &#123;
        topContainer = value;
        closeTopContainer = controller.offset > 100;
      &#125;);
    &#125;);
  &#125;

  setSelectedRadio(int val) &#123;
    setState(() &#123;
      selectedRadio = val;
    &#125;);
  &#125;

  @override
  Widget build(BuildContext context) &#123;
    return Container(
      decoration: BoxDecoration(
          gradient: LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [Colors.orange.shade200, Colors.white])),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: new AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
          leading: IconButton(
            icon: Icon(Icons.arrow_back_ios_outlined,
                color: Colors.black, size: 30),
            onPressed: () &#123;
              Navigator.of(context).pop();
            &#125;,
          ),
          title: Text(
            '日報表',
            style: TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 30,
              color: Colors.black,
            ),
          ),
        ),
        body: SingleChildScrollView(
          child: Form(
            key: _formKey,
            child:
                Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Padding(
                padding: const EdgeInsets.only(top: 25.0, left: 20.0),
                child: Container(
                  child: Text(
                    '項目名稱:',
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(top: 20.0),
                child: Center(
                  child: Text(
                    'Chuk Yuen Shopping Ctr.30 project',
                    style:
                        TextStyle(fontSize: 16, fontWeight: FontWeight.normal),
                  ),
                ),
              ),
              RadioListTile(
                value: 1,
                groupValue: selectedRadio,
                title: Text(
                  '參考編號:',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                subtitle: Text(
                  '202012170000',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.normal,
                  ),
                ),
                onChanged: (value) &#123;
                  setSelectedRadio(1);
                &#125;,
              ),
              RadioListTile(
                value: 2,
                groupValue: selectedRadio,
                title: Text(
                  '客戶編號:',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                onChanged: (value) &#123;
                  setSelectedRadio(2);
                &#125;,
              ),
              selectedRadio == 2
                  ? Padding(
                      padding: const EdgeInsets.only(
                          top: 5.0, left: 20.0, right: 20.0),
                      child: TextFormField(
                        decoration: InputDecoration(
                          border: OutlineInputBorder(
                            borderRadius: BorderRadius.circular(30.0),
                            borderSide: BorderSide.none,
                          ),
                          fillColor: Colors.white,
                          filled: true,
                          hintText: '輸入客戶編號',
                        ),
                      ),
                    )
                  : SizedBox(),
              Padding(
                padding: EdgeInsets.only(left: 20.0),
                child: Text(
                  '發布日期:',
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Padding(
                padding: EdgeInsets.only(
                    top: 10.0, left: 20.0, right: 20.0, bottom: 10.0),
                child: ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: Container(
                    height: 50,
                    color: Colors.white,
                    child: InkWell(
                      onTap: () async &#123;
                        final initialDate = DateTime.now();
                        await showDatePicker(
                          context: context,
                          initialDate: initialDate,
                          //showEXTalkDay == false ? initialDate : exTalkDay,
                          firstDate: DateTime(DateTime.now().year - 2),
                          lastDate: DateTime(DateTime.now().year + 3),
                          builder: (BuildContext context, Widget? child) &#123;
                            return Theme(
                              data: Theme.of(context).copyWith(
                                colorScheme: ColorScheme.light(),
                                primaryColor: Colors.orange,
                                textButtonTheme: TextButtonThemeData(
                                    style: TextButton.styleFrom(
                                        primary: Colors.grey)),
                              ),
                              child: child!,
                            );
                          &#125;,
                        );
                      &#125;,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.start,
                        children: [
                          Padding(
                            padding: EdgeInsets.only(left: 30),
                            child: Text(
                              '28/08/21',
                              /*showEXTalkDay == false
                            ? 'DD/MM/YY'
                            : '$&#123;exTalkDay.day&#125;/$&#123;exTalkDay.month&#125;/$&#123;exTalkDay.year&#125;'*/
                              style: TextStyle(
                                fontSize: 20.0,
                                fontWeight: FontWeight.bold,
                                color: Colors.grey[500],
                              ),
                            ),
                          ),
                          Expanded(child: SizedBox()),
                          Padding(
                            padding: EdgeInsets.only(right: 20),
                            child: Image(
                                image: AssetImage('assets/arrowupanddown.png')),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
              SizedBox(height: 10.0),
              Padding(
                padding: const EdgeInsets.only(left: 20.0),
                child: Text(
                  '天氣:',
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
              Expanded(
                flex: 1,
                child: ScrollSnapList(
                    shrinkWrap: true,
                    onItemFocus: _onItemFocus,
                    itemSize: 150,
                    scrollDirection: Axis.horizontal,
                    itemCount: weatherData.length,
                    itemBuilder: (context, index) &#123;
                      double scale = 1.0;
                      if (topContainer > 0.5) &#123;
                        scale = index + 0.5 - topContainer;
                        if (scale < 0) &#123;
                          scale = 0;
                        &#125; else if (scale > 1) &#123;
                          scale = 1;
                        &#125;
                      &#125;
                      return GestureDetector(
                        child: Opacity(
                          opacity: scale,
                          child: Transform(
                            transform: Matrix4.identity()..scale(scale, scale),
                            alignment: Alignment.bottomCenter,
                            child: Align(
                                heightFactor: 1.0,
                                alignment: Alignment.topCenter,
                                child: weatherData[index]),
                          ),
                        ),
                      );
                    &#125;),
              ),
              SizedBox(height: 20.0),
              Row(children: [
                Padding(
                  padding: const EdgeInsets.only(left: 20.0, top: 15.0),
                  child: Text(
                    '工地現場工作',
                    style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                ),
                Expanded(child: SizedBox()), //space between two elements
                Padding(
                  padding: const EdgeInsets.only(right: 20.0),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(50),
                    child: SizedBox(
                      height: 50,
                      width: 100,
                      child: ElevatedButton(
                        style: ButtonStyle(
                          backgroundColor: MaterialStateProperty.all<Color>(
                              Colors.orange.shade600),
                        ),
                        onPressed: () &#123;
                          Navigator.of(context).pop();
                        &#125;, //onpressed
                        child: Text(
                          '添加',
                          style: TextStyle(
                            fontSize: 24,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ),
                    ),
                  ),
                ),
              ]),
              SizedBox(height: 20),
              Padding(
                padding: const EdgeInsets.only(left: 20.0),
                child: Text(
                  '任務',
                  style: TextStyle(
                    fontSize: 20,
                    fontWeight: FontWeight.bold,
                  ),
                ),
              ),
            ]),
          ),
        ),
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            