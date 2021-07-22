
---
title: 'js中的==与==='
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4010'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 02:17:19 GMT
thumbnail: 'https://picsum.photos/400/300?random=4010'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我们都知道js中判断两个数是否相等有两个操作符<code>==</code>和<code>===</code>。<code>==</code>是不严格相等，在比较过程中会先将比较数进行强制类型转化，在进行值比较，而<code>===</code>是严格相等，它不会对数值的类型进行强制转换，所以理解为<code>===</code>会对数进行双重校验，先比较类型，再比较值。如果两个数的类型都不相等，那么这两个数肯定就不相等啦~</p>
<p>对于<code>===</code>这种严格相等比较的话大家基本上不会有什么异议，但是<code>==</code>真的是傻傻分不清啊！！！</p>
<p>现在整理一份便于比较的小tips，请查收~</p>
<p>首先js中有个比较特殊的数---<code>NAN</code>，这个数与任意数相比较都为<code>false</code>,hhhh,甚至与自身做比较时也是<code>false</code></p>
<pre><code class="copyable">NaN == "0"  //false
NaN == null  //false
NaN == undefined  //false
NaN == []  //false
NaN == &#123;&#125;  //false
NaN == 0  //false
NaN == false  //false
<span class="copy-code-btn">复制代码</span></code></pre>
<p>哈哈哈哈，感觉是不是还挺省事，就special,那我们怎么判断一个值是否为<code>NaN</code>呢，一般通过<code>isNaN()</code>函数判断的</p>
<p>js中还有两个特殊的数，null和undefined。这两个值互相等且自身等，其余情况与谁相比都不相等。</p>
<pre><code class="copyable">null == null  //true
null == undefined  //true
undefined == null  //true 
undefined == undefined  //true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其余的类型都是会隐式转化成对应的值来做比较的,比较规则如下表：</p>
<table>
    <tbody><tr>
        <td></td>
        <td>被比较数B</td>
        <td></td>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr>
        <td></td>
        <td></td>
        <td>Number</td>
        <td>String</td>
        <td>Boolean</td>
        <td>Object</td>
    </tr>
    <tr>
        <td>比较数A</td>
        <td>Number</td>
        <td>A === B</td>
        <td>A === ToNumber( B )</td>
        <td>A === ToNumber( B )</td>
        <td>A == ToPrimitive( B )</td>
    </tr>
    <tr>
        <td></td>
        <td>String</td>
        <td>ToNumber( A ) === B</td>
        <td>ToNumber( A )  === ToNumber( B )</td>
        <td>ToNumber( A )  === ToNumber( B )</td>
        <td>ToPrimitive( B )  == A</td>
    </tr>
    <tr>
        <td></td>
        <td>Boolean</td>
        <td>ToNumber( A ) === B</td>
        <td>ToNumber( A )  === ToNumber( B )</td>
        <td>ToNumber( A )  === ToNumber( B )</td>
        <td>ToNumber( A )  == ToPrimitive( B )  </td>
    </tr>
    <tr>
        <td></td>
        <td>Object</td>
        <td>ToPrimitive( A ) == B</td>
        <td>ToPrimitive( A ) == B</td>
        <td>ToPrimitive( A ) == ToPrimitive( B )</td>
        <td>A === B</td>
    </tr>
    <tr>
        <td></td>
    </tr>
</tbody></table>
<p>在上面的表格中，<code>ToNumber(A)</code> 尝试在比较前将参数 A 转换为数字。<code>ToPrimitive(A)</code>通过尝试调用 A 的<code>A.toString()</code> 和 <code>A.valueOf()</code> 方法，将参数 A 转换为原始值（Primitive）。</p></div>  
</div>
            