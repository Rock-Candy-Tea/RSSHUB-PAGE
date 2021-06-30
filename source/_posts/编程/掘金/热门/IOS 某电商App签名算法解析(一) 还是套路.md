
---
title: 'IOS 某电商App签名算法解析(一) 还是套路'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7385e0b7db154b0ca7f827ba61ed345e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 01 Jun 2021 21:53:38 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7385e0b7db154b0ca7f827ba61ed345e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、目标</h2>
<p>Android越来越不好玩了，年轻人，该搞搞IOS了。套路其实都是差不多的，不要被Arm汇编拦住了。</p>
<p>反正Android早就不讲武德了，重要算法都在so里面，和ios差不多了。</p>
<p>先按照之前的 [Ios逆向环境搭建 (一)] 把抓包和frida环境搞好。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7385e0b7db154b0ca7f827ba61ed345e~tplv-k3u1fbpfcp-watermark.image" alt="main.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们今天的目标还是它， <strong>sign</strong></p>
<h2 data-id="heading-1">二、步骤</h2>
<h3 data-id="heading-2">观察一下</h3>
<p>从 sign的长度和参数类型上看， sign sv st 可以看出，IOS版本的签名算法大概率和Android差不多。这能节省我们很多分析时间，直接进入主题吧。</p>
<h3 data-id="heading-3">第一步  砸壳</h3>
<p>在 frida-ios-dump 目录下面， 输入命令 **python dump.py -l ** 列出手机里面的App列表， 找到我们要搞的包名</p>
<p>然后开始运行砸壳命令，砸壳后的文件会通过 ssh拷贝到电脑上。</p>
<pre><code class="copyable">python dump.py com.3xxbuy.xxmobile
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TIP:  注意，砸壳之前请保障 SSH是通的，使用 usbmuxd 把本地的2222端口转发到iOS上的22端口,配置好 ssh免密登录</p>
<pre><code class="copyable">iproxy 2222 22
ssh -p 2222 root@127.0.0.1
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">第二步   IDA</h3>
<p>砸壳成功后，会在当前目录生成对应的 ipa文件，ipa和apk类似，也是个压缩包，我们解压先。</p>
<p>在 Payload/xx4iPhone 下面找到它的可执行文件，<strong>xx4iPhone</strong> 100多mb的这个就是了。 拖进 IDA吧</p>
<p>IDA细嚼慢咽得很长时间(<strong>很长是指好几个小时.....</strong>)，可以倒杯水，休息一把。刷刷 小视频，带薪摸鱼。</p>
<p>IDA嚼完之后， Shift + F12 ，进入 字符串窗口，我们继续查找字符串 <strong>sign=</strong></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4bdee225d13742a087dbcdc555c43412~tplv-k3u1fbpfcp-watermark.image" alt="str1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>双击一个结果，进去，在变量名称上面按 X 键 (交叉参考)，就是查看哪些地方调用这个变量。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7abaccdbe5a340dfa03bc043067d8bb5~tplv-k3u1fbpfcp-watermark.image" alt="str2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>来到 <strong>cfstr_Sign_4</strong>， 继续 X</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb066a8d4fc8411db2730880b5f7d261~tplv-k3u1fbpfcp-watermark.image" alt="str3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看这个比较像  <strong>JDCTCCHelper requestParamsWithUrl:dict:</strong>  ，进去看看，  唤起 <strong>F5大法</strong> (进入Arm汇编代码窗口之后按F5，IDA会翻译出C的伪代码)</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b21ab4c67864de1b6b0fbfd68274025~tplv-k3u1fbpfcp-watermark.image" alt="str4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>不对，没有计算过程， 把结果都翻了一遍，还没有收获。</p>
<p>试试 <strong>sv=</strong> ,因为sv这个字段比较少见，和它在一起的大概率是 sign计算过程。</p>
<p>又是一番 X ， 被我们定位到了 <strong>+[XXSignService getSignWithDic:keys:]</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f262100322b440739b7247f184d080b3~tplv-k3u1fbpfcp-watermark.image" alt="str5.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>F5一下，仔细看看这个函数。怎么看都像是sign的计算过程</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f154757dc19948a5b7f31337a05916f8~tplv-k3u1fbpfcp-watermark.image" alt="rc1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">第三步   Frida</h3>
<p>挂上我们心爱的Frida了</p>
<pre><code class="copyable">id __cdecl +[XXSignService getSignWithDic:keys:](XXSignService_meta *self, SEL a2, id a3, id a4)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个典型的ObjectC的函数就是这样， + 表示这是个类静态函数，  第一个参数指向接收Objective-C消息对象的指针。第二个参数是指向传递给对象的selector或消息的指针。  这两个参数我们暂时不用管。  第三 第四个参数才是我们要关心的真正的入参。</p>
<pre><code class="copyable">if (ObjC.available)
&#123;
    try
    &#123;
        console.log('I am Comming in!');

var className = "XXSignService";
var funcName = "+ getSignWithDic:keys:";
var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        console.log("[*] Class Name: " + className);
        console.log("[*] Method Name: " + funcName);
console.log(hook);

// /*
        Interceptor.attach(hook.implementation, &#123;
            onEnter: function(args) &#123;
var receiver = new ObjC.Object(args[0]);
                console.log("Target class : " + receiver);

var message1 = ObjC.Object(args[2]);
var message2 = ObjC.Object(args[3]);

console.log('msg1=' + message1.toString());
console.log('msg2=' + message2.toString());

            &#125;,
            onLeave: function(retval) &#123;
var message = ObjC.Object(retval);
console.log('getSignWithDic rc is:' + message.toString());

            &#125;
        &#125;);
// */


    &#125;
    catch(err)
    &#123;
        console.log("[!] Exception2: " + err.message);
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把2个入参和结果都打印出来</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/963d142b2b8f40cca87ced156c8b8c49~tplv-k3u1fbpfcp-watermark.image" alt="rc2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没毛病，就是我们想要的结果。下一次我们再说说如何RPC调用吧。</p>
<h2 data-id="heading-6">三、总结</h2>
<p>可执行文件100MB，IDA搞起来真的很慢。</p>
<p>IOS的玩法和Android差不多，特征串定位，然后挂上Frida。</p>
<p>F5大法好。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8460b68765ce4821a4714839d7974007~tplv-k3u1fbpfcp-watermark.image" alt="ffshow.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>你一定要学套路，这样才能有效的缩短学习的时间；但当你学会套路，并且开始使用套路的时候，一定要找到跟别人不一样得使用方法，这样才能让你从一堆不会飞得鸡里面，挥动翅膀，凌空飞起来，变成翱翔的鹰。</strong></p>
<p>TIP: 本文的目的只有一个就是学习更多的逆向技巧和思路，如果有人利用本文技术去进行非法商业获取利益带来的法律责任都是操作者自己承担，和本文以及作者没关系，本文涉及到的代码项目可以去 <strong>奋飞的朋友们</strong> 知识星球自取，欢迎加入知识星球一起学习探讨技术。有问题可以加我wx: <strong>fenfei331</strong> 讨论下。</p>
<p>关注微信公众号: <strong>奋飞安全</strong>，最新技术干货实时推送</p></div>  
</div>
            