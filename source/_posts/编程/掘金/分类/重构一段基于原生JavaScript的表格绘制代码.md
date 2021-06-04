
---
title: '重构一段基于原生JavaScript的表格绘制代码'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa08e28a6cc14cddaaacfbe43becf414~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 27 May 2021 22:20:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa08e28a6cc14cddaaacfbe43becf414~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>为了在CardSimulate项目中方便的显示技能和效果列表，决定重构以前编写的一段JavaScript代码——att表格绘制库，这段代码的作用是将特定的JavaScript数据对象转化为表格，支持精细的样式设置和一些复杂报表功能并且提供了自由的扩展性。可以用较新的Chrome浏览器访问https://ljzc002.github.io/Att/HTML/TEST/AttSample.html查看新版代码的例子，旧版代码的介绍见：https://www.cnblogs.com/ljzc002/p/5511510.html。</p>
<p>1、从表格类初始化表格对象</p>
<p>旧版的代码直接将表格对象作为一个全局变量，新版代码则定义了一个表格类，而每一个表格对象则是表格类的实例，这样就可以方便的在一个页面里添加多个表格对象，并有条理的管理多个表格的工作流程和属性。表格对象的初始化代码如下：</p>
<pre><code class="copyable"> 1 /**
 2  * Created by Administrator on 2015/5/11.
 3  */
 4 //动态画表类，尝试使用自包含结构
 5 //2016/8/31在表格中加入更多的格式选择
 6 //2018/10/31重构att6框架为att7版本
 7 Att7=function()
 8 &#123;
 9 
10 &#125;
11 Att7.prototype.init=function(param)//只初始化对象的属性，不实际绘制
12 &#123;
13     try
14     &#123;
15         this.base=param.base;//表格的容器对象
16         this.id=param.id;//表格的id
17         //this.left=param.left?param.left:0;//在容器对象内的左侧距离->认为tab_data和div_table完全重合
18         //this.top=param.top?param.top:0;//上部距离
19         this.rowsp=param.rowsp?param.rowsp:50;//默认每页显示50条数据，输入负值表示无限制
20         //this.page_current=param.page_current?param.page_current:0;//默认显示数据集的第一页，初始索引为0
21         this.isStripe=param.isStripe?param.isStripe:1;//这种三目运算不适用于布尔值！！！！默认奇偶行使用不同颜色
22         this.isThlocked=param.isThlocked?param.isThlocked:0;//默认不锁定表头
23         this.isCollocked=param.isCollocked?param.isCollocked:0;//默认不锁定表列
24         this.showIndex=param.showIndex?param.showIndex:1;//默认在左侧显示行号
25         this.baseColor=param.baseColor?param.baseColor:"#ffffff";//默认背景色为白色，间隔色为背景色亮度降低十六分之一
26         this.stripeColor=param.stripeColor?param.stripeColor:"#eeeeee";//有时要求奇数行和偶数行使用不同的颜色
27         this.pickColor=param.pickColor?param.pickColor:"#97ceef";//选择了某一行时要突出显示这一行
28         this.div_temp1=document.createElement("div");//这几个div用来对背景颜色进行比较，因为不同的浏览器对背景颜色的保存方式不同
29         this.div_temp1.style.backgroundColor=this.baseColor;//有的用小写字母有的用大写字母，有的用rgb+数字，所以这里主动建立div
30         this.div_temp2=document.createElement("div");//在同样的保存方式下对颜色进行比较
31         this.div_temp2.style.backgroundColor=this.stripeColor;
32         this.div_temp3=document.createElement("div");
33         this.div_temp3.style.backgroundColor=this.pickColor;
34         this.str_indexwid=param.str_indexwid?param.str_indexwid:"100px";//索引列的宽度
35         this.num_toolhei=param.num_toolhei?param.num_toolhei:80;//表格上部的工具区的高度
36        //固有属性，点击某些单元格时可以打开的小窗口
37         this.html_onclick="<div class=\"div_inmod_lim\" style=\"width: 100%;height: 100%;margin: 0px;border: 1px solid;padding: 0px;" +
38             "float: left;line-height: 20px\">    " +
39             "<div class=\"div_inmod_head\" style=\"width: 100%;height: 20px;background-color: #E0ECFF;margin:0;border: 0;padding:0;border-bottom: 1px solid\">" +
40             " <span style=\"float: left;margin-left: 2px\">详情</span>" +
41             "<BUTTON style=\'float:right;aposition:static; width: 14px;height: 14px; margin: 0;margin-top: 2px;margin-right:2px;padding: 0;" +
42             "background: url(../../ASSETS/IMAGE/close.png) no-repeat;border: 0px;vertical-align:top\' onclick=\"delete_div(\'div_bz\');\" type=submit></BUTTON> " +
43             "</div> " +
44             "<textarea class=\"div_inmod_lim_content\" style=\"width: 100%;height: 98px;overflow-x: hidden;margin:0;border: 0;padding:0\" contenteditable=\"false\"></textarea> </div>";
45         this.html_onmouseover=//鼠标移入时弹出的小文本提示框
46             "<div class=\"div_inmod_lim\" " +
47             "style=\"width: 100%;height: 100%;margin: 0px;border: 1px solid;padding: 0px;float: left;line-height: 20px\">    " +
48                 "<textarea class=\"div_inmod_lim_content\" style=\"width: 100%;height: 100%;overflow-x: hidden;margin:0;border: 0;padding:0\" contenteditable=\"false\">" +
49                 "</textarea> " +
50             "</div>";
51     &#125;
52     catch(e)
53     &#123;
54         console.log("表格初始化异常！"+e);
55         return false;
56     &#125;
57     return "ok";
58 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里设置了表格对象的各项属性，第28到33行用不显示的div解决了dom标签颜色比较问题，第37到50行定义了两个窗口小控件以备后续调用。init方法的调用方式如下：</p>
<pre><code class="copyable"> 1 var table1=new Att7();
 2     var objp=&#123;
 3         base:"div_tab",
 4         id:"table1",
 5         //left:50,
 6         //top:50,
 7         rowsp:999,
 8         isThlocked:1,
 9         isCollocked:2,//不包括索引列？-》包括
10         baseColor:"#00ff00",
11         stripeColor:"#00aa00",
12         pickColor:"#97ceef"
13     &#125;
14     if(table1.init(objp)=="ok")
15     &#123;//下面是数据显示
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、表格容器的建立：</p>
<p>表格显示时dom结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa08e28a6cc14cddaaacfbe43becf414~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其中all_base是所有表格相关元素的总容器，div_tool是表格上面的工具区，里面可以放置一些选择筛选条件的控件，div_tab是表格主体所在的区域，table1是根据数据生成的表格dom，三个div_mask是锁定表头或者锁定表列时使用的遮罩层dom。</p>
<p>使用的样式表文件如下：</p>
<pre><code class="copyable"> 1 /*专用于表格框架的样式*/
 2 body&#123;    margin: 0;    padding: 0;    border: 0;    text-align: center;    overflow: hidden;width: 100%;
 3     height: 100%;position: fixed;    font-family: verdana,arial,sans-serif;    touch-action: none;
 4     -ms-touch-action: none;font-size: 12px;min-width: 600px;&#125;
 5 #all_base&#123;min-height: 576px;min-width: 1024px;height: 100%;width:100%;position: relative;overflow-x:auto;overflow-y: hidden;&#125;
 6 /*表格的属性*/
 7 td input&#123;    height: 100%;    width: 100%;    border:0;    text-align: center;    background-color: inherit;&#125;
 8 .div_tab&#123;float: left;position: relative;width:4000px;overflow-x: hidden;overflow-y: scroll&#125;
 9 .div_tab td&#123;    text-align: center;    /*border: solid 1px #008000;*/    border-right:solid 1px #008000;    border-bottom: solid 1px #008000;
10     line-height: 16px;    font-size: 13px;    height: 24px;    padding: 1px;    background-color: inherit;    word-break: keep-all;
11 /*display: inline-block*/&#125;
12 .div_tab th&#123;    text-align: center;    /*border: solid 1px #008000;*/    line-height: 16px;    font-size: 13px;    height: 36px;
13     padding: 1px;    text-align: center;    border-right: solid 1px #008000;    border-bottom: solid 1px #008000;    word-break: keep-all;
14     white-space:nowrap;    overflow: hidden;    text-overflow: ellipsis;/*display: inline-block*/&#125;
15 .div_tab table&#123;    float: left;    width: auto;    border-right-width:0px;    border: solid 1px #008000;    table-layout: fixed;&#125;
16 .div_tab tr&#123;    width: auto;    vertical-align: middle;    /*border: solid 1px #008000;*/    padding: 1px;&#125;
17 td a&#123;    cursor: pointer;&#125;
18 td button&#123;    cursor: pointer;&#125;
19 .div_mask2&#123;    display:block;    left: 0px;    top: 0px;    /*filter: alpha(opacity=50);    opacity: 0.50;*/    overflow: hidden;/*锁定的表头表列*/
20     position: absolute;    float: left;    overflow-x: hidden&#125;
21 table&#123;    border-spacing:0;&#125;
22 .div_mask2 td&#123;    text-align: center;    /*border: solid 1px #008000;*/    border-right:solid 1px #008000;    border-bottom: solid 1px #008000;
23     line-height: 16px;    font-size: 13px;    height: 24px;    padding: 1px;    background-color: inherit;    word-break: keep-all;&#125;
24 .div_mask2 th&#123;    text-align: center;    /*border: solid 1px #008000;*/    line-height: 16px;    font-size: 13px;    height: 36px;
25     padding: 1px;    text-align: center;    border-right: solid 1px #008000;    border-bottom: solid 1px #008000;    word-break: keep-all;
26     white-space:nowrap;    overflow: hidden;    text-overflow: ellipsis;&#125;
27 .div_mask2 table&#123;    float: left;    width: auto;    border-right-width:0px;    border: solid 1px #008000;    table-layout: fixed;
28     position: absolute;&#125;
29 .div_mask2 tr&#123;    width: auto;    vertical-align: middle;    /*border: solid 1px #008000;*/    padding: 1px;&#125;
30 .combo-panel li&#123;    float:none;&#125;
31 .btn_limlen&#123;    /*float: left;*/    height: 20px;    width: 20px;    border: 1px solid;    /*margin-top: 6px;*/    /*margin-left: 4px;*/
32     background: url(../ASSETS/IMAGE/play.png) no-repeat;    position: absolute;    -moz-border-radius: 3px;      /* Gecko browsers圆角 */
33     -webkit-border-radius: 3px;   /* Webkit browsers */    border-radius:3px;            /* W3C syntax */     position: absolute;
34     top: 6px;    right: 4px;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>遗憾的是，因为上述CSS的调试过程太长，以至于已经忘记了这样设置的原因，如果您使用时出现莫名其妙的元素错位，请自己调试。</p>
<p>3、启动表格绘制</p>
<p>通过表格对象的draw方法启动表格绘制</p>
<p>调用draw方法的方式如下：</p>
<pre><code class="copyable"> 1 if(table1.init(objp)=="ok")
 2     &#123;
 3         var obj_datas=[
 4                 "测试表格",
 5                 ["测试表头","测试表头","测试表头","测试表头","测试表头","测试表头","测试表头","测试表头"],
 6                 ["str"
 7                     ,"limit"
 8                     ,["switch",["value1","text1"],["value2","text2"]]
 9                     ,["input",["class1"],["height","10px"]]
10                     ,["select","class2",[["value1","text1"],["value2","text2"],["value3","text3"]],"onChange()"]
11                     ,["check","class3"]
12                     ,["button","class4","按钮","80px",["height","10px"]]
13                     ,["a","class5",["height","10px"]]
14                 ],
15                 [100,200,300,400,500,600,700,800],
16                 ["value1","value2value2value2value2value2value2value2value2value2value2","value1","value2","value1","value2","value1","value2"],
17                 ["value1","value2","value1","value2","value1","value2","value1","value2"]
18                 ,["value1","value2","value1","value2","value1","value2","value1","value2"]
19 ];
20         table1.draw(obj_datas,0);//显示数据obj_datas的第0行
21         requestAnimFrame(function()&#123;table1.AdjustWidth();&#125;);
22     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中obj_datas是一个自定义的数据对象，这个对象可能从后端程序发送过来也可能是在前台组装生成。requestAnimFrame是截取自谷歌WebGL工具库的一个方法，用来“延时一会”，等待浏览器完成表格容器渲染后，再调整表格尺寸从而使表格布局紧密。</p>
<p>延时代码如下：</p>
<pre><code class="copyable"> 1 // Copyright 2010, Google Inc.
 2 window.requestAnimFrame = (function() &#123;
 3     return window.requestAnimationFrame ||
 4         window.webkitRequestAnimationFrame ||
 5         window.mozRequestAnimationFrame ||
 6         window.oRequestAnimationFrame ||
 7         window.msRequestAnimationFrame ||
 8         function(/* function FrameRequestCallback */ callback, /* DOMElement Element */ element) &#123;
 9             window.setTimeout(callback, 1000/60);
10         &#125;;
11 &#125;)();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、表格绘制代码的介绍：</p>
<p>a、首先做一些和表格翻页有关的准备工作：</p>
<pre><code class="copyable"> 1 Att7.prototype.draw=function(data,page_current)//实际绘制dom元素
 2 &#123;
 3     this.totalpages=0;//记录下一共有多少页
 4     if(this.rowsp>0)
 5     &#123;
 6         this.totalpages=Math.ceil((data.length-4)/this.rowsp);
 7     &#125;
 8     if(this.totalpages==0)
 9     &#123;
10         this.totalpages=1;
11     &#125;
12     //计算当前页数
13     if(page_current<0)
14     &#123;
15         alert("到达数据首页！");
16         this.page_current=0;
17     &#125;
18     else if(page_current>=this.totalpages)
19     &#123;
20         alert("到达数据末尾");
21         this.page_current=this.totalpages-1;
22     &#125;
23     else
24     &#123;
25         this.page_current=page_current;
26     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p> 因为att将所有dom标签的生成工作放在浏览器端，所以可以一次性将所有数据从后台读取到前端，由前端JavaScript程序进行分页操作。（而传统表格绘制工具多把dom标签生成放在后台程序中，为了降低后台压力，分页操作多在数据库层面进行）</p>
<p>翻页方法代码如下：</p>
<pre><code class="copyable"> 1 //翻页处理
 2 Att7.prototype.ChangePage=function(flag)
 3 &#123;
 4     document.body.style.cursor='wait';
 5     switch(flag)//不同的翻页动作对应不同的页号处理
 6     &#123;
 7         case "0":
 8         &#123;
 9             this.page_current=0;
10             break;
11         &#125;
12         case "+":
13         &#123;
14             this.page_current++;
15             break;
16         &#125;
17         case "-":
18         &#123;
19             this.page_current--;
20             break;
21         &#125;
22         case "9999":
23         &#123;
24             this.page_current=9999;
25             break;
26         &#125;
27     &#125;
28     this.draw(this.data,this.page_current);
29     document.getElementById('t_page_span').innerHTML=this.totalpages;
30     try &#123;//万一没有定义
31         AdjustColor();
32     &#125;
33     catch(e)
34     &#123;
35 
36     &#125;
37     document.getElementById('c_page_span').innerHTML=this.page_current+1;
38     document.body.style.cursor='default';
39     var _this=this;
40     try
41     &#123;
42         requestAnimFrame(function () &#123;
43             _this.AdjustWidth()
44         &#125;);
45     &#125;
46     catch(e)
47     &#123;
48 
49     &#125;
50 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据ChangePage方法的不同参数，可以进行四种不同的翻页操作，您可以再需要的地方建立四个按钮来对应这些操作，而翻页操作实际上只是改变了参数的draw方法。t_page_span和c_page_span是两个span标签，用来显示总页数和当前页数。AdjustColor是一个可选的方法，在绘制表格后遍历单元格，根据需求改变符合某种条件的单元格的颜色。（这里并未使用）</p>
<p>b、在开始绘制之前清理以前可能绘制过的id相同的表格：</p>
<pre><code class="copyable"> 1 //接着上面的翻页准备
 2 this.data=data;//表格的数据集
 3     var tab_data;//table标签
 4     var tab_colmask;//列锁定遮罩标签
 5     if (document.getElementById(this.id))//如果已有该表
 6     &#123;//清理已有的dom
 7         tab_data= document.getElementById(this.id);
 8         var parent = tab_data.parentNode;
 9         parent.removeChild(tab_data);
10         if(document.getElementById("div_thmask"))//删除锁定表头的遮罩层
11         &#123;
12             var div =document.getElementById("div_thmask");//看来这样的设定还不能支持一个页面中同时存在多个锁定表头表格
13             div.parentNode.removeChild(div);
14         &#125;
15         if(document.getElementById("tab_mask2"))//删除锁定表列的遮罩层
16         &#123;
17             var tab =document.getElementById("tab_mask2");
18             tab.parentNode.removeChild(tab);
19         &#125;
20         if(document.getElementById("div_thmask3"))//
21         &#123;
22             var tab =document.getElementById("div_thmask3");
23             tab.parentNode.removeChild(tab);
24         &#125;
25     &#125;
26     tab_data = document.createElement("table");//重新建立table标签
27     tab_data.id = this.id;
28     tab_data.cellPadding = "0";
29     tab_data.cellSpacing = "0";
30     tab_data.style.position = "absolute";
31     //tab_data.style.top = this.top + "px";
32     //tab_data.style.left = this.left + "px";
33     var div_table;//包含表格的容器元素
34 
35     var obj=this.base;//这个属性可能是id字符串也可能是对象本身
36     if((typeof obj)=="string"||(typeof obj)=="String")
37     &#123;
38         div_table = document.getElementById(obj);
39     &#125;
40     else
41     &#123;
42         div_table=obj;
43     &#125;
44     div_table.innerHTML="";
45     div_table.appendChild(tab_data);//将table标签放入容器里
46     this.div_table=div_table;
47     tab_data = document.getElementById(this.id);
<span class="copy-code-btn">复制代码</span></code></pre>
<p> </p>
<p>c、表格表头的绘制与遮罩原理</p>
<p>在一个简单的表格里绘制表头并不复杂：</p>
<pre><code class="copyable"> 1 var tr1 = document.createElement("tr");//填写表头（接着清理代码）
 2     if(this.showIndex==1)//如果显示索引列
 3     &#123;
 4         this.InsertaTHStr(tr1, "第"+(this.page_current+1) + "页",this.str_indexwid);//IE8中缺少参数会报错
 5     &#125;
 6     for (var k = 0; k < data[1].length; k++)
 7     &#123;
 8         this.InsertaTHStr(tr1, data[1][k],(data[3][k]+"px"));
 9     &#125;
10     tab_data.appendChild(tr1);//将tr放入table
11     tr1.style.backgroundColor=this.baseColor;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果选择显示索引列，则在表头的最左侧多插入一个th，InsertaTHStr方法用来向指定tr中插入th，参数分别是tr对象、列名、列宽，这里的data也就是之前构造的数据集。</p>
<p>InsertaTHStr代码如下：</p>
<pre><code class="copyable"> 1 //一些工具方法
 2 /**
 3  * 向一个表行中添加字符型表头元素
 4  * @param tr 表行ID
 5  * @param str 添加字符
 6  * @param wid 列宽（字符型px）
 7  * @constructor
 8  */
 9 Att7.prototype.InsertaTHStr=function(tr,str,wid)
10 &#123;
11     var th=document.createElement("th");
12     th.style.width=wid?wid:"200px";
13     if(str==null)
14     &#123;
15         str="";
16     &#125;
17     th.appendChild(document.createTextNode(str));
18     tr.appendChild(th);
19 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然而当需要锁定表头或者锁定表列时，事情变得复杂，接着绘制表头的代码：</p>
<pre><code class="copyable"> 1 this.arr_lock=[];//all_base左右滑动时需要调整位置的元素
 2     this.arr_locky=[];
 3     if(this.isThlocked==1)//绘制锁定表头的遮罩层，它的内容和原表格的表头是一样的
 4     &#123;
 5         var div_thmask=document.createElement("div");
 6         div_thmask.className="div_mask2";
 7         div_thmask.id="div_thmask";
 8         div_thmask.style.zIndex="200";
 9         var div_parent=div_table.parentNode;
10         this.div_parent=div_parent;
11         div_thmask.style.top=(compPos2(div_table).top-parseInt(div_table.style.height.split("p")[0]))+this.top+"px";//定位添加的遮罩层
12         div_thmask.style.left=compPos2(div_table).left+this.left+"px";
13         div_thmask.style.width="6000px";//遮罩的最大宽度
14         div_thmask.style.height="42px";
15         div_thmask.style.top=this.num_toolhei+"px";
16         //div_thmask.getElementsByTagName("table")[0].style.backgroundColor=this.baseColor;
17 
18         var tab_thmask= document.createElement("table");
19         var tr_thmask=document.createElement("tr");
20         if(this.showIndex==1)//如果不禁止索引列
21         &#123;
22             this.InsertaTHStr(tr_thmask, "第" + (this.page_current + 1) + "页", this.str_indexwid);//IE8中缺少参数会报错
23         &#125;
24         for (var k = 0; k < data[1].length; k++)
25         &#123;
26             this.InsertaTHStr(tr_thmask, data[1][k],(data[3][k]+"px"));
27         &#125;
28         tab_thmask.appendChild(tr_thmask);
29         tab_thmask.style.backgroundColor=this.baseColor;
30         div_thmask.appendChild(tab_thmask);
31         div_parent.appendChild(div_thmask);
32     &#125;
33     if(this.isCollocked>0)//绘制锁定表列的遮罩层，估计不需要外包装的div，可以和data_table共享div_table（考虑到层数决定这样做）
34     &#123;
35         this.arr_lock.push(["tab_mask2",1,0]);//第一个参数是要锁定的标签的id，第二个是是否锁定，第三个是标签的初始水平偏移量
36         this.arr_lock.push(["div_bz",0,0]);
37         tab_colmask= document.createElement("table");
38         tab_colmask.cellPadding = "0";
39         tab_colmask.cellSpacing = "0";
40         tab_colmask.style.position = "absolute";
41         tab_colmask.className="div_mask2";
42         tab_colmask.id="tab_mask2";
43         tab_colmask.style.zIndex="150";
44         tab_colmask.style.top="0px";
45         tab_colmask.style.backgroundColor=this.baseColor
46         var tr_mask= document.createElement("tr");//创造一个占位用的表头行
47         if(this.showIndex==1)//如果不禁止索引列
48         &#123;
49             this.InsertaTHStr(tr_mask, "第" + (this.page_current + 1) + "页", this.str_indexwid);
50         &#125;
51         for (var k = 0; k < this.isCollocked-1; k++)
52         &#123;
53             this.InsertaTHStr(tr_mask, data[1][k],(data[3][k]+"px"));
54         &#125;
55         tab_colmask.appendChild(tr_mask);
56     &#125;
57     //如果同时锁定了表头和左侧的表列
58     if((this.isThlocked==1)&&(this.isCollocked>0))
59     &#123;
60         this.arr_lock.push(["div_thmask3",1,0]);
61         var div_thmask=document.createElement("div");
62         div_thmask.className="div_mask2";
63         div_thmask.id="div_thmask3";
64         div_thmask.style.zIndex="250";
65         var div_parent=div_table.parentNode;
66         div_thmask.style.top=(compPos2(div_table).top-parseInt(div_table.style.height.split("p")))+"px";//定位添加的遮罩层
67         div_thmask.style.left=compPos2(div_table).left+"px";
68         div_thmask.style.width="4000px";
69         div_thmask.style.height="42px";
70         div_thmask.style.top=this.num_toolhei+"px";
71 
72         var tab_thmask= document.createElement("table");
73         tab_thmask.style.backgroundColor=this.baseColor;
74         var tr_thmask=document.createElement("tr");
75         if(this.showIndex==1)//如果不禁止索引列
76         &#123;
77             this.InsertaTHStr(tr_thmask, "第" + (this.page_current + 1) + "页", this.str_indexwid);//IE8中缺少参数会报错
78         &#125;
79         for (var k = 0; k < this.isCollocked-1; k++)
80         &#123;
81             this.InsertaTHStr(tr_thmask, data[1][k],(data[3][k]+"px"));
82         &#125;
83         tab_thmask.appendChild(tr_thmask);
84         div_thmask.appendChild(tab_thmask);
85         div_parent.appendChild(div_thmask);
86     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现表头表列锁定的思路是这样的：首先all_base的大小固定为all_base的容器的大小（在这里等于窗口大小），然后把div_table设置的足够宽（默认4000px），而高度则设为all_base高度减div_tools高度的有限值，这样当table的行数较多且div_table获得焦点时即可用鼠标滚轮控制div_table的内容的上下滚动，而因为div_table的宽度超过all_base，div_table的上下滑动条被隐藏起来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/defa343f57b74cbcb42d0c4a272ac601~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>在div_table的内容上下滚动时，因为div_thmask和div_thmask3在div_table外相对于all_base定位，所以不会受div_table滚动的影响，再将z-index设高一些，看起来就是表格内容滚动而表头锁定不变。</p>
<p>至于表列锁定，首先禁用all_base的上下滑动，只保留左右滑动，因为div_table比all_base宽，所以all_base的左右滑动条一直存在，监听all_base滑动条的滑动事件，在每次滑动时调整div_mask2的水平位置，即可达到看起来锁定了表列的效果。</p>
<p>在同时锁定了表头和表列时，div_thmask3位于这几个遮罩的最上层，表现二者共同起作用的效果。</p>
<p>all_base滑动的响应方法如下：</p>
<pre><code class="copyable"> 1 Att7.prototype.ScrollLock=function()//拖动滑动条时，弹出层随拖动一同移动
 2 &#123;
 3     var mask2left=0;
 4     var mask2top=0;
 5     var scrollleft=document.getElementById("all_base").scrollLeft;//scrollLeft指滑动条向右滑动的距离
 6     var scrolltop=document.getElementById("all_base").scrollTop;
 7     var arr_lock=this.arr_lock;
 8     var arr_locky=this.arr_locky;
 9     var leng=arr_lock.length;
10     for(var i=0;i<leng;i++)
11     &#123;
12         if(arr_lock[i][1]==1)
13         &#123;
14             //$("#"+arr_lock[i][0]).css("left",mask2left+scrollleft+arr_lock[i][2]+"px");
15             document.getElementById(arr_lock[i][0]).style.left=mask2left+scrollleft+arr_lock[i][2]+"px";
16         &#125;
17     &#125;
18     var leng2=arr_locky.length;
19     for(var i=0;i<leng2;i++)
20     &#123;
21         if(arr_locky[i][1]==1)
22         &#123;
23             //$("#"+arr_locky[i][0]).css("top",mask2top+scrolltop+arr_locky[i][2]+"px");
24             document.getElementById(arr_locky[i][0]).style.top=mask2top+scrolltop+arr_locky[i][2]+"px";
25         &#125;
26     &#125;
27 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在实际使用中发现，虽然锁定遮罩里的内容和原表格里的内容相同，但实际渲染时总会出现尺寸偏差，所以在完成渲染后执行AdjustWidth方法重新调整遮罩的宽度：</p>
<pre><code class="copyable"> 1 //不断修正让遮罩层的宽高和底层一致
 2 Att7.prototype.AdjustWidth=function()
 3 &#123;
 4     if(document.getElementById("div_thmask"))
 5     &#123;
 6         var ths_mask = document.getElementById("div_thmask").getElementsByTagName("th");
 7         var ths = document.getElementById(this.id).getElementsByTagName("th");
 8         if (ths[0].offsetWidth) &#123;//有宽度说明浏览器已经完成了渲染操作
 9             this.div_table.style.height=this.div_parent.offsetHeight-this.num_toolhei-12+"px";//调整div_table高度
10             var leng = ths.length;
11             for (var i = 0; i < leng; i++) &#123;
12                 try &#123;
13                     ths_mask[i].style.width = (ths[i].offsetWidth - 3) + "px";
14                 &#125;
15                 catch (e) &#123;
16                     //i--;
17                     continue;
18                 &#125;
19             &#125;
20             if (document.getElementById("div_thmask3")) &#123;
21                 var div_thmask3 = document.getElementById("div_thmask3").getElementsByTagName("th");
22                 var leng2 = div_thmask3.length;
23                 for (var i = 0; i < leng2; i++) &#123;
24                     div_thmask3[i].style.width = (ths[i].offsetWidth - 3) + "px";
25                 &#125;
26             &#125;
27             if (document.getElementById("tab_mask2"))
28             &#123;
29                 var trs_mask = document.getElementById("tab_mask2").getElementsByTagName("tr");
30                 var trs = document.getElementById(this.id).getElementsByTagName("tr");
31                 var leng3 = trs.length;
32                 for (var i = 1; i < leng3; i++)
33                 &#123;
34                     trs_mask[i].style.height =(trs[i].offsetHeight)+"px";
35                 &#125;
36             &#125;
37         &#125;
38         else &#123;//如果还没有完成渲染，则再延时调用一次
39             var _this=this;
40             requestAnimFrame(function () &#123;
41                 _this.AdjustWidth()//需要注意的是延时操作或者事件触发时，原来的this对象已经随着时间的推移被释放掉了，所以用_this保持这个对象
42             &#125;);
43         &#125;
44     &#125;
45 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果您想为表格添加动态调整列宽功能，可以在列宽变化后调用这个方法；或者如果您想在浏览器尺寸变化后保持div_table和all_bas的紧密贴合也可以将这个方法设为resize事件的响应。</p>
<p>d、绘制最简单的表格内容：</p>
<pre><code class="copyable">//接着上面的表头绘制
if (this.rowsp > 0)//默认必须要分页，数据集的第一行是表名、第二行是列名、第三行是列设定、第四行是列宽、第五行开始是数据
    &#123;
        var rows=this.rowsp;//每一页多少行
        var pages=this.page_current;//当前页
        var collock=this.isCollocked;//锁定几个表列
        var count=0;//标记经过了几个没有数据源的列，存在按钮等不填写源数据的列时，data[2]会比data[l]长，为了让后面的类型和数据对应上，应该用m减去count！
        var count_none=0;//标记经过了几个使用数据源但不显示的列，
        for (var l = 4 + pages * rows; l < data.length && (l - pages * rows) < rows + 4; l++)
        &#123;//遍历当前页中的每一条数据
            //dataObj2.push(data[l]);
            count=0;//绘制每一行时都把标记数设为0，其后每检测到一个标记就+1，data[l][m+count]从数据源取数
            count_none=0;
            var tr2 = document.createElement("tr");//填写一个表行
            var tr_mask = document.createElement("tr");//准备给遮罩层用
            if (l % 2 == 0&&this.isStripe==1)//偶数的数据行显示为间隔色
            &#123;
                tr2.style.backgroundColor = this.stripeColor;
                tr_mask.style.backgroundColor = this.stripeColor;
            &#125;
            else
            &#123;
                tr2.style.backgroundColor = this.baseColor;
                tr_mask.style.backgroundColor = this.baseColor;
            &#125;
            if(this.showIndex==1)//如果不禁止索引列
            &#123;
                this.InsertaTDPick(tr2, l - 3 + "");//这个是序号
                this.InsertaTDPick2(tr_mask, l - 3 + "", this.id);//遮罩层的序号
            &#125;

            for (var m = 0; m < data[2].length; m++)//一行中的一个单元格，这里可能有多种变化，在length范围外的数据列不会被考虑
            &#123;//根据数据源的第三个元素中存储的DOM信息，为数据的每一列设置不同的控件类型！！！！
                try
                &#123;
                    if (data[2][m] == "str") //简单的字符类型，要限制下宽度！
                    &#123;
                        this.InsertaTDStr(tr2, data[l][m - count],(data[3][m-count_none]+"px"));
                        if(this.isCollocked>0&&(m+1)<this.isCollocked)
                        &#123;
                            this.InsertaTDStr(tr_mask, data[l][m - count],(data[3][m-count_none]+"px"));
                        &#125;
                    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在实际使用中发现每一行数据集的元素数和表格每一行的列数并不总是能一一对应，有时表格的列数比数据集元素多，比如不包含数据集的控件，有时表格宽度比数据集短，比如某一列数据需要设定为“不可见”，为此设置了count和count_none两个计数器对表格和数据集的索引进行调整。</p>
<p>接下来设置每一个数据tr的颜色，并在需要时向tr推入显示行号的索引列单元格。</p>
<p>然后遍历数据集这一行的每个数据，根据设置的单元格类型，向tr中推入单元格，对于最简单的str型单元格使用InsertaTDStr方法向tr中添加，其代码如下：</p>
<pre><code class="copyable"> 1 /**
 2  * 向一个表行中添加字符型单元格元素
 3  * @param tr 表行ID
 4  * @param str 添加字符
 5  * @param wid 列宽
 6  * @constructor
 7  */
 8 Att7.prototype.InsertaTDStr=function(tr,str,wid)
 9 &#123;
10     var td=document.createElement("td");
11     td.style.width=wid?wid:"200px";
12     if(str==null)
13     &#123;
14         str="";
15     &#125;
16     td.appendChild(document.createTextNode(str));
17     tr.appendChild(td);
18 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，如果有锁定表列，则也向表列锁定遮罩里推入这个td。</p>
<p>e、前面的代码中还出现了InsertaTDPick和InsertaTDPick2方法，它们的作用是通过点击原表格或锁定表列遮罩上的行号突出显示某行数据：</p>
<pre><code class="copyable"> 1 //一个可以被选中的单元格，选中后改变单元格所在表行的颜色以突出显示
 2 Att7.prototype.InsertaTDPick=function (tr,str)
 3 &#123;
 4     var td=document.createElement("td");
 5     td.appendChild(document.createTextNode(str));
 6     td.style.cursor="crosshair";
 7     var _this=this;
 8     td.onclick=function()
 9     &#123;//考虑到浏览器可能擅自更改背景颜色样式的字符串表示格式，使用一个不显示的div进行比对
10         if(td.parentNode.style.backgroundColor!=_this.div_temp3.style.backgroundColor)
11         &#123;//如果还没变色
12             td.parentNode.style.backgroundColor=_this.pickColor;
13         &#125;
14         else
15         &#123;
16             if(_this.isStripe==1)
17             &#123;
18                 //如果已经变色则恢复原本颜色
19                 if(parseInt(td.innerHTML)%2==0)
20                 &#123;
21                     td.parentNode.style.backgroundColor = _this.baseColor;
22                 &#125;
23                 else
24                 &#123;
25                     td.parentNode.style.backgroundColor = _this.stripeColor;
26                 &#125;
27             &#125;
28             else
29             &#123;
30                 td.parentNode.style.backgroundColor = _this.baseColor;
31             &#125;
32         &#125;
33     &#125;;
34     tr.appendChild(td);
35 &#125;
36 //这个给遮罩层用,id是表实体的id
37 Att7.prototype.InsertaTDPick2=function (tr,str,id)
38 &#123;
39     var td=document.createElement("td");
40     td.appendChild(document.createTextNode(str));
41     td.style.cursor="crosshair";
42     td.style.width="50px";
43     var _this=this;
44     td.onclick=function()
45     &#123;//526DA5
46         if(td.parentNode.style.backgroundColor!=_this.div_temp3.style.backgroundColor)
47         &#123;
48             td.parentNode.style.backgroundColor=_this.pickColor;//修改遮罩层
49             ChangeTable(td,_this.pickColor);
50         &#125;
51         else
52         &#123;
53             if(_this.isStripe==1)
54             &#123;
55                 if(parseInt(td.innerHTML)%2==0)
56                 &#123;
57                     td.parentNode.style.backgroundColor = _this.baseColor;
58                     ChangeTable(td,_this.baseColor);
59                 &#125;
60                 else
61                 &#123;
62                     td.parentNode.style.backgroundColor = _this.stripeColor;
63                     ChangeTable(td,_this.stripeColor);
64                 &#125;
65             &#125;
66             else
67             &#123;
68 
69             &#125;
70         &#125;
71     &#125;;
72     function ChangeTable(obj,color)//遮罩层变化之后，原表格也要变化
73     &#123;
74         var trs=document.getElementById(id).getElementsByTagName("tr")//找实体表然后去修改
75         var leng=trs.length;
76         for(var i=1;i<leng;i++)
77         &#123;
78             if(obj.innerHTML==trs[i].getElementsByTagName("td")[0].innerHTML)
79             &#123;
80                 trs[i].getElementsByTagName("td")[0].parentNode.style.backgroundColor=color;
81             &#125;
82         &#125;
83     &#125;
84     tr.appendChild(td);
85 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>f、自定义多样的单元格类型</p>
<p>att定义了多种常用的复杂报表单元格，也支持您添加自己的单元格类型，时间有限，这里只举两个例子：</p>
<p>limit单元格：数据长度正常时原样显示，如果数据长度超过单元格宽度太多，则显示缩略文本，同时在单元格里插入一个按钮，点击按钮弹出小对话框显示完整内容：</p>
<pre><code class="copyable">1 else if(data[2][m] == "limit")//限制字符长度不能过长
2                     &#123;
3                         this.InsertaTDStr_lim(tr2, data[l][m - count],(data[3][m-count_none]+"px"));
4                         if(collock>0&&(m+1)<collock)
5                         &#123;
6                             this.InsertaTDStr_lim(tr_mask, data[l][m - count],(data[3][m-count_none]+"px"));
7                         &#125;
8                     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> 1 //限制宽度
 2 Att7.prototype.InsertaTDStr_lim= function(tr,str,wid,charwid)
 3 &#123;//
 4     var td=document.createElement("td");
 5     td.style.width=wid?wid:"200px";
 6     td.style.position="relative";
 7     if(str==null)
 8     &#123;
 9         str="";
10     &#125;
11     var num_wid=parseInt(wid.split("px")[0]);
12     var input1 = document.createElement("input");
13     input1.type="text";
14     input1.style.border = 0;
15     input1.style.width =num_wid+"px" ;//控件宽度
16     input1.style.textAlign = "center";
17     input1.style.backgroundColor="transparent";
18     input1.style.float="left";
19     input1.value=str;
20     input1.readOnly=true;
21     /*input1.onfocus=function(evt)&#123;
22      this.blur();这样就不能复制粘贴了！
23      &#125;*/
24 
25     if(!charwid)//如果没有设置字宽
26     &#123;
27         charwid=10;
28     &#125;
29     if((str.length*charwid)>(num_wid*2))//如果文字的长度超过了单元格宽度的两倍
30     &#123;
31         //td.title=str;
32         //td.overflow="hidden";
33         //str=(str.substr(0,(num_wid*2/10).toFixed()) +"...");
34         //尝试在右侧加一个弹出小按钮？
35         //str=(str.substr(0,(num_wid*2/10).toFixed()) );
36         input1.style.width =(num_wid-30)+"px" ;
37         td.appendChild(input1);
38         var btn =document.createElement("button");
39         btn.className="btn_limlen";
40         btn.title=str;
41         var _this=this;
42         btn.onclick=function()//通过点击打开的弹出框需要一个关闭按钮，通过鼠标移入打开的弹出框则随移出自动关闭
43         &#123;
44             /*if(clipboardData) &#123;
45              clipboardData.clearData();
46              clipboardData.setData("text", str);
47              &#125;
48              else */
49             /*
50              if(event.clipboardData)
51 
52              &#123;//火狐？
53              event.clipboardData.clearData();
54              event.clipboardData.setData("text/plain", str);
55              alert("内容已复制到剪贴板");
56              &#125;
57              else if(window.clipboardData)
58              &#123;//IE
59              window.clipboardData.clearData();
60              window.clipboardData.setData("text", str);
61              alert("内容已复制到剪贴板");
62              &#125;
63              */
64             //clipboardData.getData("text");
65             var evt=evt||window.event||arguments[0];
66             cancelPropagation(evt);
67             var obj=evt.currentTarget?evt.currentTarget:evt.srcElement;
68             if(delete_div("div_bz")>0)//清空可能已经显示的其他小窗口
69             &#123;
70                 //return;
71             &#125;
72             Open_div("", "div_bz", 240, 120, 0, 0, obj, "div_tab");//自编的一个弹出小窗口方法（旧版）
73             //var target=&#123;top:,left:&#125;//lim保持不变，尝试添加lim2
74             //Open_div2("div_bz", "div_bz", 240, 120, 0, 0, obj, "div_tab");
75             document.querySelectorAll("#div_bz")[0].innerHTML = _this.html_onclick;//向弹出项里写入结构（之前初始化阶段定义的小控件）
76             document.querySelectorAll("#div_bz .div_inmod_lim_content")[0].innerHTML = str;
77         &#125;
78         td.appendChild(btn);
79     &#125;
80     else
81     &#123;
82         td.appendChild(input1);
83     &#125;
84 
85     tr.appendChild(td);
86 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>select：单元格里是一个下拉框，用户改变选项后触发某些事件</p>
<pre><code class="copyable"> 1 else if (data[2][m][0] == "select")//单元格是一个下拉框
 2                     &#123;
 3                         var td2 = document.createElement("td");
 4                         //td2.style.width = "100px";
 5                         td2.style.width=(data[3][m-count_none]+"px");
 6                         var select = document.createElement("select");
 7                         select.className = data[2][m][1];
 8                         select.style.width = "100px";
 9                         select.selectedIndex=0;
10                         var temp_i=0;//用来暂存下面的i
11                         for (var i = 0; i < data[2][m][2].length; i++)
12                         &#123;
13                             var option = document.createElement("option");
14                             option.innerHTML = data[2][m][2][i][0];
15                             if(data[2][m][2][i][1]) &#123;//如果有的话也不介意设置一个value
16                                 option.value = data[2][m][2][i][1];
17                             &#125;
18                             select.appendChild(option);
19                             if(data[2][m][2][i][1]==data[l][m - count]||data[2][m][2][i][0]==data[l][m - count])//后台传过来的可能是value也可能是text！！
20                             &#123;//如果这个选项和数据集里的数据相符，则默认把这个选项选中
21                                 option.selected="selected";
22                                 select.selectedIndex=i;
23                                 temp_i=i;
24                             &#125;
25                         &#125;
26                         listenEvent(select,"change",select_onchange);//监听选项变化
27                         select.datachange=data[2][m][3];
28                         function select_onchange()
29                         &#123;
30                             var evt = evt || window.event||arguments[0];
31                             cancelPropagation(evt);//发现如果不阻断事件，会引发button1的click相应！！？？
32                             var obj=evt.currentTarget?evt.currentTarget:evt.srcElement;
33                             //dataObj2[parseInt(this.parentNode.parentNode.firstChild.innerHTML)%150-1][parseInt(this.className.split("*")[1])]=this.value;
34                             eval((obj.getAttribute("datachange")?obj.getAttribute("datachange"):obj.datachange));
35                         &#125;
36                         /*select.onchange=function()
37                          &#123;
38                          var evt = evt || window.event;
39                          cancelPropagation(evt);//发现如果不阻断事件，会引发button1的click相应！！？？
40                          //dataObj2[parseInt(this.parentNode.parentNode.firstChild.innerHTML)%150-1][parseInt(this.className.split("*")[1])]=this.value;
41                          eval(data[2][m][3]);
42                          &#125;*/
43                         td2.appendChild(select);
44                         tr2.appendChild(td2);
45                         if(collock>0&&(m+1)<collock)//对于遮罩层
46                         &#123;
47                             /*var td2a = document.createElement("td");
48                              td2a.style.width=(data[3][m-count_none]+"px");
49                              var selecta=select.cloneNode(true);
50                              selecta.datachange=data[2][m][3];
51                              td2a.appendChild(selecta);*/
52                             var td2a=td2.cloneNode(true);//克隆dom元素
53                             var selecta=td2a.childNodes[0];
54                             selecta.datachange=data[2][m][3];
55                             selecta.selectedIndex=temp_i;
56                             tr_mask.appendChild(td2a);
57                             listenEvent(selecta,"change",select_onchange);
58                         &#125;
59                     &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、总结</p>
<p>基本完成了att的重构工作，旧版中使用jQuery的地方都替换成了原生的JavaScript方法，虽然原生方法的兼容性不如JQuery，但考虑到要配合兼容性更窄的WebGL使用，这些兼容性损失可以忽略。重构的代码没有经过充分测试，可能存在各种问题，您可以访问https://ljzc002.github.io/Att/HTML/TEST/AttSample.html测试部分单元格类型。</p>
<p> </p></div>  
</div>
            