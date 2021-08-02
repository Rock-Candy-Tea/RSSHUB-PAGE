
---
title: 'PC端  React使用高德地图实现点击事件标记经纬度'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8930'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 20:02:02 GMT
thumbnail: 'https://picsum.photos/400/300?random=8930'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>使用插件</strong>：<code>react-amap</code><br>
<strong>版本号：</strong><code>1.2.8</code></p>
<ol>
<li>安装依赖<code>npm install react-amap@1.2.8</code></li>
<li>使用的文件中引入</li>
</ol>
<p>reactMap.js文件</p>
<pre><code class="copyable">import &#123; Map, Marker &#125; from 'react-amap'
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>使用</li>
</ol>
<pre><code class="copyable">//构造函数声明position
constructor(props) &#123;
  super(props)
  this.state = &#123;
    position: &#123;
      longitude: '',
      latitude: ''
    &#125;,
  &#125;
&#125;

//获取坐标存入position中
getLocalAddress = (lng, lat) => &#123;
    this.setState(&#123;
        position: &#123;
           longitude: lng,
           latitude: lat
        &#125;
    &#125;)
&#125;

render()&#123;
  const &#123;position&#125; = this.state

  const events = &#123;
    created: (ins) => &#123; console.log(ins) &#125;,
    click: (e) => this.getLocalAddress(e.lnglat.lng, e.lnglat.lat)
  &#125;

  return (
    <div style=&#123;&#123;width: '100%', height: 500&#125;&#125;>
      <Map amapkey=&#123;'f1ef05bc86c26bf0690da7f7fdd7edd5'&#125; events=&#123;events&#125;>
        <Marker
          position=&#123;position ? position : null&#125;
          clickable=&#123;true&#125;
          draggable=&#123;true&#125;
        />
      </Map>
    </div>
  )
<span class="copy-code-btn">复制代码</span></code></pre>
  <br>
   4. 小结
<p>  以前没有接触过地图的功能  用到这个插件怎么也实现不了 点击地图上的坐标就能获取到经纬度 并且标记上地图坐标  后来逐渐看多了官方文档之后发现是自己将event事件用错了地方<br>
  在这里例子中 之前用这个插件的时候自己将events事件放在了Marker组件标签 这个组件里没有click事件 后来发现 应该是在Map组件标签上添加events事件</p>
<p>哈哈哈哈 总算是实现出来了</p></div>  
</div>
            