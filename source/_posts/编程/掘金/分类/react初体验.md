
---
title: 'react初体验'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd1f310f4e29444aba2bfb4da061a354~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 17:33:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd1f310f4e29444aba2bfb4da061a354~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第24天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd1f310f4e29444aba2bfb4da061a354~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>安装react的环境</p>
<pre><code class="copyable">npm install -g create-react-app
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后利用脚手架建立项目demo01</p>
<pre><code class="copyable">create-react-app demo01
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（关于create-react-app很慢的问题）由于某原因,在拉取各种资源时,往往会巨慢</p>
<p>解决方案是换源,虽然平常使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Flink.jianshu.com%3Ft%3Dhttps%253A%252F%252Fnpm.taobao.org%252F" target="_blank" rel="nofollow noopener noreferrer" title="https://link.jianshu.com?t=https%3A%2F%2Fnpm.taobao.org%2F" ref="nofollow noopener noreferrer">cnpm</a>来代替npm,但也只是使用新的指令而已，而在寻求create-react-app的相关配置希望修改registry时失败了，最后发现create-react-app指令默认调用npm，于是直接把npm的register给永久设置过来就好了，这样使用cnpm或者npm就没差别了。</p>
<pre><code class="copyable">npm config set registry https://registry.npm.taobao.org
-- 配置后可通过下面方式来验证是否成功
npm config get registry
-- 或npm info express
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9db35d3ca5594748a737df3594c80c92~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>设置成功后，再执行create-react-app my-app，就会有惊喜。</p>
<p>\</p>
<p><strong>react的优缺点：</strong></p>
<p>优点：</p>
<p>1、JSX写在javascript里，执行更快，编译为javascript代码时进行优化</p>
<p>2、类型更安全，编译过程如果出错就不能编译，及时发现错误</p>
<p>3、JSX编写模板更加简单快速（不要跟vue比）</p>
<p>\</p>
<p>注意：</p>
<p>1、JSX必须要有根节点</p>
<p>2、正常的普通HTML元素要小写，如果是大写，默认认为是组件</p>
<p>\</p>
<p><strong>JSX表达式</strong></p>
<p>1、由HTML元素构成</p>
<p>2、中间如果需要插入变量用&#123;&#125;，且不用写""或者''</p>
<p>3、&#123;&#125;中间可以使用表达式</p>
<p>4、&#123;&#125;中间表达式中可以使用JSX对象</p>
<p>5、属性和html内容一样都是用&#123;&#125;来插入内容</p>
<p>\</p>
<p>JSX的class是className, 而不是直接class（当然，直接class也不会出错）</p>
<pre><code class="copyable">import React from 'react'
import ReactDOM from 'react-dom'

const classStr = "regBg"
const element = (
    <div>
        <h1 className=&#123;"abc " + classStr&#125;>hello world</h1>
    </div>
)

ReactDOM.render(element, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df14221f0d064e6a917e32608e9bdc1d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果classname是数组形式 =></p>
<p>如：</p>
<pre><code class="copyable">import React from 'react'
import ReactDOM from 'react-dom'

const classStr = ["regBg", "red"]
const element = (
    <div>
        <h1 className=&#123;classStr&#125;>hello world</h1>
    </div>
)

ReactDOM.render(element, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>则会报错， &#123;&#125;内可写数组，可无法识别</p>
<p>结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f585b28a2964898a7d03d8dbc34cf90~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果数组的拆分再合并，则可以 如 =></p>
<pre><code class="copyable">import React from 'react'
import ReactDOM from 'react-dom'

const classStr = ["regBg", "red"].join(' ')
const element = (
    <div>
        <h1 className=&#123;classStr&#125;>hello world</h1>
    </div>
)

ReactDOM.render(element, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>结果：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b87361fde0ea454a97ef27e8d71e630a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>JSX的style</strong></p>
<p>如果在JSX里面写style，是没有-的，并且第二个字母需要大写（borderBottom: 1px solid #ddd;）</p>
<pre><code class="copyable">import React from 'react'
import ReactDOM from 'react-dom'

const exampleStyle = &#123;
    background: "skyblue",
    borderBottom: "1px solid #red"
&#125;

const element = (
    <div>
        <h1 style=&#123;exampleStyle&#125;>hello world</h1>
    </div>
)

ReactDOM.render(element, document.getElementById('root'))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、class、style中，不可以存在多个class或者style属性</p>
<pre><code class="copyable"><div class='abc' class=&#123;active&#125;></div>   // 错误的表示
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、style样式中，如果存在多个单词的属性组合， 第二个单词开始， 首字母大写, 也可以用引号''写起来</p>
<pre><code class="copyable">const exampleStyle = &#123;
  backgroundColor: "skyblue",
  borderBottom: "4px solid red",
  'background-image': "url(https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png)"
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、注释</p>
<p>必须要括号的表达式内书写，否则报错 => &#123;/* 代码 */&#125;</p></div>  
</div>
            