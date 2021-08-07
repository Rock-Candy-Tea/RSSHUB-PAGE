
---
title: 'Mustache学习笔记一'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51cd3b4e743c4124a425f0743834c430~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 08:27:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51cd3b4e743c4124a425f0743834c430~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p><strong>在初学vue的时候，我就一直在想为什么在<code><span> Message: &#123;&#123; msg &#125;&#125; </span></code>中使用&#123;&#123;&#125;&#125;就可以将msg替代为对应数据对象上 'msg' property 的值？它的底层原理又是什么？为什么需要这样的语法呢？毕竟vue官网上只简单的说了一句：使用“Mustache”语法 (双大括号) 的文本插值。所以我就去查了一下Mustache语法，才发现Mustache并不是vue的专属语法，它的出现比vue.js更早，也有其他的框架使用了Mustache语法</strong></p>
<h1 data-id="heading-0"><strong>1.什么是模版引擎</strong></h1>
<p><strong>JavaScript 模板引擎是在数据与界面分离的情况下将数据转变成视图的最优雅的解决方案（目前为止，如果有更好的在下面评论区提醒我一下😂）</strong></p>
<h1 data-id="heading-1">2.Mustache简介</h1>
<p><strong>Mustache翻译过来的中文意思是胡子，只是因为&#123;&#123;&#125;&#125; 看起来很像人的胡子（我都呆了😱）。他是一种没有逻辑的模板语法，它只有标签没有逻辑处理（轻逻辑），包括像if else判断 或者for 循环之类也不会去做处理。因为它是基于javascript 实现的模板引擎，所以可以使用JavaScript的地方就可以使用Mustache模版引擎。包括web浏览器、服务器环境（node）。也有很多框架在使用Mustache（如vue.js）,并对其进行封装优化（如vue.js中的v-for,在Mustache中是无法使用for循环的）</strong></p>
<h1 data-id="heading-2">3.历史变革：将数据变为视图的方案</h1>
<p><strong>俗话说没有对比就没有伤害，既然我们说Mustache好，那么它究竟好在哪呢，我们与之前的方案做一下对比就知道了，我们来举个🌰，实现下面的效果</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/51cd3b4e743c4124a425f0743834c430~tplv-k3u1fbpfcp-watermark.image" alt="目标的副本.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">1.纯DOM法</h2>
<p><strong>试试用纯DOM法来写一次就深有体会了（代码很长，你忍一下）</strong></p>
<pre><code class="copyable">  <div id="container"></div>
  <script>
    const data = [&#123;
      title: '疾风剑豪简介',
      name: '亚索',
      address: '艾欧尼亚',
      passive: '被动：浪客之道',
      qSkill: '斩刚闪',
      wSkill: '风之壁障',
      eSkill: '踏前斩',
      rSkill: '狂风绝息斩',
    &#125;,&#123;
      title: '盲僧简介',
      name: '李青',
      address: '艾欧尼亚',
      passive: '40%攻速加成',
      qSkill: '天音波/回音击',
      wSkill: '金钟罩/铁布衫',
      eSkill: '天雷破/摧筋断骨',
      rSkill: '中国足球',
    &#125;]
    const container = document.getElementById('container')
    const len = data.length
    for (let i = 0; i < len; i++) &#123;
      const item = data[i]
      const item1 = document.createElement('div')
      item1.className = 'item_box'
      const info1 = document.createElement('h1')
      info1.innerText = item.title
      const hName = document.createElement('h2')
      hName.innerText = '姓名：'+item.name
      const aName = document.createElement('h2')
      aName.innerText = '地点：'+item.address
      const ui1 = document.createElement('ui')
      const qli1 = document.createElement('li')
      qli1.innerText ='被动：'+item.passive
      const qli2 = document.createElement('li')
      qli2.innerHTML = 'q：'+item.qSkill
      const qli3 = document.createElement('li')
      qli3.innerText = 'w：'+item.wSkill
      const qli4 = document.createElement('li')
      qli4.innerText = 'e：'+item.eSkill
      const qli5 = document.createElement('li')
      qli5.innerText = 'r：'+item.rSkill
      item1.appendChild(info1 )
      item1.appendChild(hName )
      item1.appendChild(aName )
      ui1.appendChild(qli1)
      ui1.appendChild(qli2)
      ui1.appendChild(qli3)
      ui1.appendChild(qli4)
      ui1.appendChild(qli5)
      item1.appendChild(ui1)
      container.appendChild(item1)
    &#125;
  </script>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>我们可以看到，我们需要通过id 获取DOM节点，并在for循环创建与数据对应每一个节点，然后通过<code>+</code>斩断连接数据，被创建的节点都是孤儿节点，我们还需要手动追加到父节点中。</strong></p>
<h2 data-id="heading-4">2.数组join连接法</h2>
<pre><code class="copyable">  <script>
    const container = document.getElementById('container')
    const len = data.length 
    for (let i = 0; i < len; i++) &#123;
      const item = data[i];
      container.innerHTML += [
        '<div class="item_box">',
          '<h1>'+item.title+'</h1>',
          '<h2>姓名：'+item.name+'</h2>',
          '<h2>地点：'+item.address+'</h2>',
          '<ul>',
            '<li>被动：'+item.passive+'</li>',
            '<li>q：'+item.qSkill+'</li>',
            '<li>w：'+item.wSkill+'</li>',
            '<li>e：'+item.eSkill+'</li>',
            '<li>r：'+item.rSkill+'</li>',
          '</ul>',
        '</div>',
      ].join('')
    
    &#125;
  </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>因为双引号是不能换行的，所以我们将每一行看成是数组中的每一项，然后通过join连接拼成一个字符串。并且在每一项中我们可以通过<code>+</code>的方法斩段连接我们需要填充的内容。比纯的DOM方法简洁了不少</strong></p>
<h2 data-id="heading-5">3.es6反引号法</h2>
<p>在es6中新增了一个反引号，在反引号中是可以换行的所以我们就不需要先将其放入到数组中再转换成字符串来。并且新增了<code>$&#123;&#125;</code>语法糖我们也可以不用<code>+</code>去斩断连接字符串了.</p>
<pre><code class="copyable">  for (let i = 0; i < len; i++) &#123;
      const item = data[i]
      container.innerHTML += 
        `<div class="item_box">
          <h1>$&#123;item.title&#125;</h1>
          <h2>姓名：$&#123;item.name&#125;</h2>
          <h2>地点：$&#123;item.address&#125;</h2>
          <ul>
            <li>被动：$&#123;item.passive&#125;</li>
            <li>q：$&#123;item.qSkill&#125;</li>
            <li>w：$&#123;item.wSkill&#125;</li>
            <li>e：$&#123;item.eSkill&#125;</li>
            <li>r：$&#123;item.rSkill&#125;</li>
          </ul>
        </div>`
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">4.我们来总结一下曾经出现过的将数据转变成视图的方法，可以看出来对于程序开发者来说，代码量在逐步减少：</h1>
<p><strong>1.纯DOM法需要创建节点并且追加到父节点上（性能最优，因为后面的数组join法或者反引号法解析完成之后还是需要进行DOM操作，但是对于开发者来说太过麻烦了，其性能差别也不是特别大，或者说不必要为了这一点性能而花费大量的时间去操作DOM）</strong></p>
<p><strong>2.因为innerHTML 属性设置或返回表格行的开始和结束标签之间的 HTML，而这个HTML必须是字符串类型。我们直接写的话，如果是比较复杂的结构我们必须写在一行中，这样无法看清结构也不利于开发，偏偏双引号中无法换行但是数组却可以，并且数组通过join方法可以转为字符串，这样就解决了双引号带来的的问题，字符串又可以通过<code>+</code>连接，所以我们在循环中（上诉例子）拼接HTML字符串</strong></p>
<p><strong>图1:双引号中的换行我们可以看到很明显的错误提示：</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a1f89131eee40b99faf0bab9cb92f72~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 上午12.23.43.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>图二：通过数组换行</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62e807d577674b839c3f834e4e8b163e~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 上午12.24.41.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>3.es6新增的反引号可以换行，所以我们不需要通过数组转成字符串了，而且<code>$&#123;&#125;</code> 可以替代<code>+</code>斩断连接字符串</strong></p>
<p><strong>图三：反引号换行：</strong></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e87c11a414d745bb8b546ef8e5589a28~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-07 上午12.23.56.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            