
---
title: '谈谈JavaScript中对象属性及堆栈的的概念'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e458314a727b4b9d9362479c4b062429~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 16:55:46 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e458314a727b4b9d9362479c4b062429~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">前言</h2>
<p>大家好哇，今天我们来谈谈JavaScript中对象属性及堆栈的概念，对于非科班出身的小伙伴而言，这其中的概念还是很容易被搞混的，所以今天我们就来好好谈一下这个问题。</p>
<h2 data-id="heading-1">文章目标</h2>
<p>先来看一下本文的目标吧，大神请绕道，因为本文基本摘自我刚入行时的笔记哦~</p>
<h3 data-id="heading-2">重点</h3>
<pre><code class="copyable">1. 能够获取和设置对象属性的值
2. 能够遍历对象
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">了解</h3>
<pre><code class="copyable">1. 知道内存中分为栈和堆两个区域
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">操作对象</h2>
<p>操作对象比较简单，熟练基本的操作对象方法即可。</p>
<h3 data-id="heading-5">获取对象属性的值</h3>
<p>注意: 如果对象中没有的属性,返回的是undefined。</p>
<pre><code class="copyable">var obj = &#123;
    name: '小明',
    age: 20
&#125;
alert(obj.name)    // '小明'
alert(obj.sex)     // undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">给对象添加属性并赋值</h3>
<pre><code class="copyable">var obj = &#123;
    name: 'ls'
    age: 20
&#125;
// 给对象添加属性并赋值
obj.sex = '男'
console.log(obj)  // &#123;name: 'ls', age: 28, sex:'男'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">通过中括号语法操作对象的属性</h3>
<p>语法：对象 [ '属性名' ]</p>
<pre><code class="copyable">var stu01 = &#123;
  name:'小白',
  age:28,
  sex:true,
  getInfo:function()&#123;
    return '我的名字叫：'+this.name + '，年龄：'+ this.age + '，性别：' + this.sex
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取操作如下：</p>
<pre><code class="copyable">alert(stu01.name)    // 小白
alert(stu01['name'])    // 小白
alert(stu01.getInfo())    // 我的名字叫小白,年龄28,性别true
alert(stu01['getInfo']())    // 我的名字叫小白,年龄28,性别true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>赋值，以下两种方式书写代码的作用是一样的：</p>
<pre><code class="copyable">stu01.name = '小黑'
stu01['name'] = '小黑'
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">遍历对象中的所有属性</h3>
<blockquote>
<p>通过for..in循环,遍历对象的属性</p>
<p>语法: for( var 变量名 in 被遍历的对象)&#123; 循环执行的代码 &#125;</p>
</blockquote>
<pre><code class="copyable">var obj = &#123;
    name: 'zs',
    age: 18,
    sayHi:function()&#123;
        console.log('hi');
    &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>对象中有几个属性,for循环就会执行几次</p>
<p>循环过程中,会把对象中的属性依次赋值给key变量</p>
<p>在循环中使用中括号语法</p>
</blockquote>
<pre><code class="copyable">for(var key in obj) &#123;
  console.log(key + "==" + obj[key]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">删除对象中的某个属性</h3>
<pre><code class="copyable">var obj = &#123;
     name: 'zs',
    age: 18
&#125;
console.log(obj.age)    // 18
delete obj.age
console.log(obj.age)    // undefined
console.log(obj)    // &#123;name: 'zs'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">内存中的栈空间和堆空间</h2>
<blockquote>
<p>js的所有代码都要加载到内存中执行,而内存中其实也分了区域,比如,内存中有栈 和 堆两个区域</p>
<p>js中的6种数据类型,又分为了两大类: 基本数据类型和引用数据类型</p>
<p>栈相当于是地址，堆相当于是实际存储的地方</p>
</blockquote>
<ul>
<li>基本数据类型存储在栈空间中</li>
<li>引用数据类型存储在堆空间中</li>
</ul>
<p>图解如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e458314a727b4b9d9362479c4b062429~tplv-k3u1fbpfcp-watermark.image" alt="栈和堆内存示意图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">基本数据类型和引用数据类型传参</h3>
<h4 data-id="heading-12">基本数据类型赋值</h4>
<pre><code class="copyable">var num1 = 1;
var num2;
num2 = num1;  //把num1的值克隆一份赋值给num2
console.log(num2); //1
<span class="copy-code-btn">复制代码</span></code></pre>
<p>图解如下：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1651fcb5524e4b39a022ef82dfc5b80d~tplv-k3u1fbpfcp-watermark.image" alt="基本赋值.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">引用数据类型赋值</h4>
<pre><code class="copyable">var obj = &#123;
    name: 'zs'
&#125;
var num2
num2 = obj
console.log(num2) // &#123; name: 'zs'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>图解如下：
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89933ecc7e88456eba118b1599467960~tplv-k3u1fbpfcp-watermark.image" alt="引用赋值.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">后记</h2>
<p>你好哇，我是南极大冰块，一个技术与颜值成正比的前端工程师，崇尚一针见血的搞定前端问题，希望我的博客有帮助到了你。</p>
<p>关注我，前端路途一起走。嘿哈~😛</p></div>  
</div>
            