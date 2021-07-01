
---
title: '前端开发：在JavaScript 中JSON.stringify()和JSON.parse() 的使用总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1751af29a1134e8492249965c2f118de~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 23:49:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1751af29a1134e8492249965c2f118de~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<h3 data-id="heading-0">前言</h3>
<p>在前端开发过程中，对于JSON的处理使用的场景是比较多的，也是比较常见的需求。JSON 是用于存储和传输数据的格式，JSON 通常用于服务端向网页传递数据，而且它是一种轻量级的数据交换格式。尤其是在JS开发相关的时候，将JSON 数据转换为 JavaScript 对象是非常常见的处理方式。那么本文就来分享一下前端对于JSON处理的常用方法JSON.stringify()和JSON.parse() 的使用总结。</p>
<h3 data-id="heading-1">功能介绍</h3>
<h4 data-id="heading-2">1、JSON.stringify()</h4>
<p>JSON.stringify() 方法用于将 JavaScript对象转换为 JSON 字符串，也就是从一个对象中解析出来字符串。</p>
<h4 data-id="heading-3">2、JSON.parse()</h4>
<p>JSON.parse() 方法用于将数据转换为 JavaScript 对象，也就是从一个字符串中解析出来对象。</p>
<p>简单来讲，JSON.stringify()和JSON.parse()的作用是相对的、互斥的，例如用JSON.stringify()将对象a变成了字符串b，那么就可以 直接用JSON.parse()将字符串b还原成对象a。</p>
<h3 data-id="heading-4">语法及参数</h3>
<h4 data-id="heading-5">1、JSON.stringify()</h4>
<p>语法： <code>JSON.stringify(value[, replacer[, space]])</code></p>
<p>参数：</p>
<ul>
<li>value:必传参数， 想要转换的 JavaScript 值（一般为对象或数组）。</li>
<li>replacer: 可选参数，用于转换结果的函数或数组。 space: 可选参数，文本添加缩进、空格和换行符。space 也可以使用非数字，如：\t。</li>
</ul>
<p>返回值：
返回的是包含 JSON 文本的字符串。</p>
<h4 data-id="heading-6">2、JSON.parse()</h4>
<p>语法：<code>JSON.parse(text[, reviver])</code></p>
<p>参数：</p>
<ul>
<li>text:必传参数， 想要转换的标准有效的JSON 字符串。</li>
<li>reviver: 可选参数，一个转换结果的函数，将为对象的每个成员调用此函数。</li>
</ul>
<p>返回值：返回的是JavaScript 对象。</p>
<h3 data-id="heading-7">实例</h3>
<h4 data-id="heading-8">1、JSON.stringify()的使用</h4>
<h5 data-id="heading-9">对象转字符串</h5>
<pre><code class="copyable">var str = &#123;"name":"sanzhanggui", "age":"30","gender":"male","phone":"15290331111"&#125;;
basic_str = JSON.stringify(str);
console.log(basic_str); //输出字符串
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">2、JSON.parse()的使用</h4>
<h5 data-id="heading-11">字符串转数组</h5>
<pre><code class="copyable">var jdList = [];
var str1 = '[&#123;\"createBy\":70446,\"createDate\":1622092153440,\"updateBy\":70446,\"updateDate\":1622092153440,\"remarks\":null,\"id\":4037,\"templateId\":61,\"fieldId\":132,\"fieldName\":\"JD\",\"fieldType\":\"1\",\"fieldLength\":999,\"fieldSetup\":null,\"isRequired\":\"1\",\"isVisible\":\"1\",\"isFixed\":\"1\",\"reason\":null,\"lineAccounted\":null,\"value\":\"444\",\"options\":null,\"sortNum\":8,\"status\":\"1\",\"clearable\":true,\"templates\":\"col-sm-6\"&#125;,&#123;\"createBy\":70446,\"createDate\":1622092153440,\"updateBy\":70446,\"updateDate\":1622092153440,\"remarks\":null,\"id\":4039,\"templateId\":61,\"fieldId\":129,\"fieldName\":\"需求时间\",\"fieldType\":\"5\",\"fieldLength\":1,\"fieldSetup\":null,\"isRequired\":\"1\",\"isVisible\":\"1\",\"isFixed\":\"1\",\"reason\":null,\"lineAccounted\":null,\"value\":\"2021-06-22T16:00:00.000Z\",\"options\":null,\"sortNum\":10,\"status\":\"1\",\"templates\":\"col-sm-6\"&#125;]';

jdList = JSON.parse(str1);
console.log(jdList); //输出数组的两条数据
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1751af29a1134e8492249965c2f118de~tplv-k3u1fbpfcp-watermark.image" alt="002.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-12">字符串转对象</h5>
<pre><code class="copyable">var jdData = &#123;&#125;;
var str2 = '&#123;\"createBy\":70446,\"createDate\":1622092153440,\"updateBy\":70446,\"updateDate\":1622092153440,\"remarks\":null,\"id\":4037,\"templateId\":61,\"fieldId\":132,\"fieldName\":\"JD\",\"fieldType\":\"1\",\"fieldLength\":999,\"fieldSetup\":null,\"isRequired\":\"1\",\"isVisible\":\"1\",\"isFixed\":\"1\",\"reason\":null,\"lineAccounted\":null,\"value\":\"444\",\"options\":null,\"sortNum\":8,\"status\":\"1\",\"clearable\":true,\"templates\":\"col-sm-6\"&#125;';

jdData = JSON.parse(str2);
console.log(jdList); //输出对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">应用场景</h3>
<h4 data-id="heading-14">JSON.stringify()的使用</h4>
<p>1、假如后台Java对应的RequestMapping参数列表中的参数为一个对象，前台有多个传输，那就需要通过JSON.stringify()进行处理，否则会出现参数解析异常报错。
2、判断数组是否包含某对象，或者判断对象是否相等。</p>
<pre><code class="copyable">//判断数组是否包含某对象
var data = [ &#123;name:'123'&#125;, &#123;name:'abc'&#125;, &#123;name:'@#$'&#125;];
var value = &#123;name:'abc'&#125;;
JSON.stringify(data).indexOf(JSON.stringify(value)) !== -1;   //true
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">//判断两个数组或者对象是否相等
var  a = [a,b,c],
var  b = [a,b,c];
JSON.stringify(a) === JSON.stringify(b);     //true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、通过让localStorage/sessionStorage可以存储对象格式的数据。localStorage/sessionStorage默认的情况下只能存储字符串类型的数据，但是在实际开发的时候需要存储的数据多为对象类型，那么就可以利用json.stringify()将对象转为字符串再进行缓存存储，在取缓存数据的时候，通过json.parse()配合使用把数据转回成对象就可以。</p>
<pre><code class="copyable">//缓存数据
function setStorage(key, value)&#123;
    window.localStorage.setItem(key,JSON.stringify(value));
&#125;;
//取出缓存数据
function getStorage(key)&#123;
    let value = JSON.parse(window.localStorage.getItem(key));
    return value;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、实现对象的深拷贝。在开发过程中，若怕影响到原始数据，通常操作是深拷贝出一份原始数据做任意的操作，其实可以通过使用JSON.stringify()与JSON.parse()来实现深拷贝。</p>
<pre><code class="copyable">//深拷贝
function deepCopy(data) &#123;
    let _data = JSON.stringify(data),
        dataCopy = JSON.parse(_data);
    return dataCopy;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、JSON.stringify()与toString()的使用对比，虽然二者都可将目标值转为字符串，但本质上还是有区别的，比如</p>
<pre><code class="copyable">let array = [1,2,3];
JSON.stringify(array);  // '[1,2,3]'
array.toString();  // 1,2,3
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接着，JSON.stringify()的受体更多的是对象，但toString()虽可把数组转为字符串，但并不能对&#123;name:'@#$'&#125;这类的对象实现想要的操作效果，toString()的受体更多的是数字。</p>
<h4 data-id="heading-15">JSON.parse()的使用：</h4>
<p>1、假如前台向后台请求，然后后台返回一大堆的字符串数据，此时前台页面渲染需要将后台返回一大堆的字符串数据以对象的形式渲染出来，这时候就需要使用JSON.parse()进行处理。</p>
<p>2、注意事项：在使用JSON.parse()的时候需要注意一下，由于此方法是把JSON字符串转换成对象，所以该字符串必须符合JSON格式，即键值都必须使用双引号包裹才行，不然会引起报错。</p>
<p>以上就是本章的全部内容，欢迎关注三掌柜的微信公众号“程序猿by三掌柜”，三掌柜的新浪微博“三掌柜666”，欢迎关注！</p></div>  
</div>
            