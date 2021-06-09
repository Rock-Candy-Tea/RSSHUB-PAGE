
---
title: 'loader和plugin的区别'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1273'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 19:43:12 GMT
thumbnail: 'https://picsum.photos/400/300?random=1273'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第7天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h3 data-id="heading-0">子组件和父组件componentDidMount哪一个先执行</h3>
<p>子组件的componentDidMount先执行。</p>
<pre><code class="copyable">import React, &#123; Component &#125; from 'react';
class Test extends Component&#123;
    componentWillMount()&#123;
        console.log('子组件将要挂载')
    &#125;
    render()&#123;
        return(<p>&#123;this.props.index&#125;</p>)
    &#125;
&#125;
 
 
export default class TestPanel extends Component&#123;
    componentDidMount()&#123;
        console.log('父组件挂载完毕');
    &#125;
    render()&#123;
        return(
            <div>
                <Test index=&#123;1&#125;/>
                <Test index=&#123;2&#125;/>
                <Test index=&#123;3&#125;/>
            </div>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">wepack中loader和plugin的区别</h3>
<h4 data-id="heading-2">loader：</h4>
<p>loader从字面的意思理解，是 加载 的意思。
由于webpack 本身只能打包commonjs规范的js文件，所以，针对css，图片等格式的文件没法打包，就需要引入第三方的模块进行打包。loader虽然是扩展了 webpack ，但是它只专注于转化文件（transform）这一个领域，完成压缩，打包，语言翻译。loader是运行在NodeJS中。仅仅只是为了打包，仅仅只是为了打包，仅仅只是为了打包，重要的话说三遍！</p>
<p>如：css-loader和style-loader模块是为了打包css的</p>
<p>babel-loader和babel-core模块时为了把ES6的代码转成ES5</p>
<p>url-loader和file-loader是把图片进行打包的。</p>
<h4 data-id="heading-3">plugin是做什么的</h4>
<p>plugin完成的是loader不能完成的功能，这是废话，没有说清楚。
plugin也是为了扩展webpack的功能，但是 plugin 是作用于webpack本身上的。而且plugin不仅只局限在打包，资源的加载上，它的功能要更加丰富。从打包优化和压缩，到重新定义环境变量，功能强大到可以用来处理各种各样的任务。webpack提供了很多开箱即用的插件：CommonChunkPlugin主要用于提取第三方库和公共模块，避免首屏加载的bundle文件，或者按需加载的bundle文件体积过大，导致加载时间过长，是一把优化的利器。而在多页面应用中，更是能够为每个页面间的应用程序共享代码创建bundle。
插件可以携带参数，所以在plugins属性传入new实例。</p>
<p>如：针对html文件打包和拷贝（还有很多设置）的插件：html-webpack-plugin。
不但完成了html文件的拷贝，打包，还给html中自动增加了引入打包后的js文件的代码（），还能指明把js文件引入到html文件的底部等等。</p>
<p>代码如下：</p>
<pre><code class="copyable">plugins:[   
//对html模板进行处理，生成对应的html,引入需要的资源模块
new HtmlWebpackPlugin(&#123;
    template:'./index.html',//模板文件，即需要打包和拷贝到build目录下的html文件
    filename:'index.html',//目标html文件
    chunks:['useperson'],//对应加载的资源,即html文件需要引入的js模块
    inject:true//资源加入到底部，把模块引入到html文件的底部
    &#125;)
]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">从运行时机的角度区分</h4>
<p> 1 . loader运行在打包文件之前（loader为在模块加载时的预处理文件）
 2.  plugins在整个编译周期都起作用。</p></div>  
</div>
            