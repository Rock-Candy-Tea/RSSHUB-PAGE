
---
title: '用Hexo+Github Pages搭建私人博客_重下git配置个人信息以及报错'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b7d56ab70f540b6bc5546ed5cea55b5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 05:56:53 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b7d56ab70f540b6bc5546ed5cea55b5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<blockquote>
<p>每日一句，送给最珍贵的你：
人生没有目的，只有过程，所谓的终极目的是虚无的。《查拉图斯特拉如是说》-尼采</p>
</blockquote>
<p>之前重装了系统，关于博客也是得重新配置，这里给大家说明一下在重新下好Git后我们需要重新将个人账号相关信息输入进去，也是自己的用户名和邮箱，即在git任意的界面下执行如下命令：</p>
<p><code>git config --global user.name "此处填你的用户名" </code></p>
<p><code>git config --global user.email "此处填写你的邮箱" </code></p>
<p>无报错即说明配置成功了。</p>
<p>然后便是在将自己的博客文件上传到Github，但是在配置个人账号后上传后还是会出现报错，报错内容如下：</p>
<p><code>报错为：bash: hexo: command not found</code></p>
<p>解决思路：本着能解决问题就不重来的原则，首先先检查node和npm是否正常，依次输入以下命令：</p>
<p><code>node -v</code></p>
<p><code>npm -v</code></p>
<p>若能显示版本信息则表明node和npm是没有问题的，如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b7d56ab70f540b6bc5546ed5cea55b5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最后小编也是直接重新下的hexo，新建一个文件夹，然后直接运行如下命令下载hexo（下载会有点慢）:</p>
<p><code>npm install hexo -cli -g</code></p>
<p>下载好后即可上传到Github啦。</p>
<p>最近在看《黑天鹅-如何应对不可知的未来》, 分享一下作者的观点:</p>
<ol>
<li>世界上的事情可简单的分为两种: 平均斯坦和极端斯坦.</li>
<li>平均斯坦里，个体对结果的影响不大，只有大量的个体才对结果有影响。极端斯坦里，个体能够对整体产生不可思议的影响。</li>
<li>举两个例子：随机取一百个人，得到平均身高，这个数不会因为某一两个人而出现大的变动，这属于平均斯坦；如果把身高换成财富，结果就大不相同了，可能因为比尔盖茨的加入而使得平均数成万倍的增长，这属于极端斯坦。</li>
<li>绝大多数社会问题属于极端斯坦，换句话说社会变量是信息化的，不是物理的。</li>
</ol>
<p>有一位朋友建议我，寻找一份报酬不受时间限制的工作。面包师必须不断的烘烤面包才能得到更多的收入; 而 J.K.罗琳 不用在每次读者购买哈利波特的时候再写一遍。这也是脑力劳动与体力劳动的分界线。</p>
<p><strong>按照这个理论, Coder也分为两种: 幸苦搬砖型和一劳永逸型. 对号入座的事情我就不做了, 显然我属于前者.</strong></p></div>  
</div>
            