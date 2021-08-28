
---
title: 'Unity粒子特效系列-下雨预制体做好了，拿走直接就用！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43ff5e81a1ae4934893dd9748ebc6b00~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 04:44:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43ff5e81a1ae4934893dd9748ebc6b00~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p><strong>这是我参与8月更文挑战的第27天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
</blockquote>
<h2 data-id="heading-0">👉关于作者</h2>
<blockquote>
<p>众所周知，人生是一个漫长的流程，不断克服困难，不断反思前进的过程。在这个过程中会产生很多对于人生的质疑和思考，于是我决定将自己的思考，经验和故事全部分享出来，以此寻找共鸣！！！<br>
专注于Android/Unity和各种游戏开发技巧，以及各种资源分享（网站、工具、素材、源码、游戏等）</p>
</blockquote>
<h2 data-id="heading-1">👉即将学会</h2>
<p>利用粒子系统实现下雨效果。</p>
<p>我们要掌握核心科技，提高生产力。其中关键的内容就是下落速度，大小变化，颜色变化，渲染器的选择</p>
<h2 data-id="heading-2">👉效果预看</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/43ff5e81a1ae4934893dd9748ebc6b00~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<h2 data-id="heading-3">👉背景</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b81891abd3f6454cb7204274784b2075~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/7001089080742117406" loading="lazy" referrerpolicy="no-referrer">一个普通的下雨天气。</p>
<p>🙎小芝：你看，下雨了。</p>
<p>🙈小空：恩，真是太爽了，我特别喜欢下雨。</p>
<p>🙎小芝歪头：为什么呀？</p>
<p>🙈小空沉思：因为下雨让人很舒服，更关键的是下雨天安静可以做特别的事。</p>
<p>🙎小芝：特别的事？（小芝忽然惊讶） 啊，不会是，不会是那个吧，怎么可以做那种事？我们还没有…… 啊！啊！啊！还害羞啊！</p>
<p>🙈小空：你有病啊。在那嘀咕啥呢？我说的是睡觉。</p>
<p>🙎小芝：啊？就单纯的睡觉吗？没别的？</p>
<p>🙈小空：当然，据不知道是谁研究表明-长期维持着专注的注意力会让人精神疲劳，人们精神耗损后需要通过一些方式来补充精力。当身处有柔和之美的自然环境中时，人们不自觉地将大脑放空，不为达成任何目的地去体验天人合一。在这种感觉下，人们不再斤斤计较于世俗的价值，不再烦心功名利禄，正是这些体验让人们耗损的精力得到补充，注意力得到恢复。</p>
<p>🙎小芝心想：我好歹也是一姑娘，你就不能有点其他想法吗？我很被动啊！</p>
<p>……</p>
<p>聊着聊着，小空又打开了电脑。</p>
<h2 data-id="heading-4">👉案例环境</h2>
<p>Unity 2020.3 LTS系列</p>
<h2 data-id="heading-5">👉实践过程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4d1b82f0d6a44cea6e75ea8806a27c8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p>基本属性持续时间要久一点，因为要保证雨从上一直到下</p>
<p>雨会一直下，所以要开启循环播放（默认是开启的）</p>
<p>雨是有大有小的，所以起始大小我们取一个范围区间（0.2-1）来模拟出不同大小</p>
<p>雨的颜色是透明白的且不一致，所以其实颜色（白色改变的是透明度A）我们要有个区间，让它随机生成</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f11202cd0ff2467aa2eb126836967151~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p>发射和形状和啥可说的。要想下大雨单位时间产生的粒子就多一些。</p>
<p>下图左侧是随单位时间产生的粒子数为1000 右侧是10000</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/374ed6de69a644b4bb77503594a697c9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/7001089080742117406" loading="lazy" referrerpolicy="no-referrer">雨肯定是往下落的，所以我们需要加一个受力，Y轴是上下的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/77443a02347e42d0bf9faf485217b786~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/7001089080742117406" loading="lazy" referrerpolicy="no-referrer">接着就是生命周期内颜色以及大小。颜色不变化，变化的是透明度，大小嘛，随心喽，看你心中的雨想要什么样的.</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c9d569496934bbd8208cd2c2f7efd7b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/7001089080742117406" loading="lazy" referrerpolicy="no-referrer">最关键的当然是渲染器了，没她是显示不出效果的。</p>
<p>因为我们需要对离子进行伸缩操作，所以使用伸展 Billboard模式</p>
<p>将长度进行缩放</p>
<p>将最大粒子大小调小一点，毕竟雨没那么大。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eac8749126ce4bd58365ab21622d57ee~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<p><img alt title="点击并拖拽以移动" src="https://juejin.cn/post/7001089080742117406" loading="lazy" referrerpolicy="no-referrer">好啦，到这下雨就结束了，运行下看看吧。</p>
<p>其实这还不算真实的下雨，下雨地上不仅有积水，还有声音，风，等等内容。</p>
<p>不过不要急，下节我们继续，做出更深入的下雨效果。</p>
<h2 data-id="heading-6">👉源码地址</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdownload.csdn.net%2Fdownload%2Fqq_27489007%2F19787322%3Fspm%3D1001.2014.3001.5503" target="_blank" rel="nofollow noopener noreferrer" title="https://download.csdn.net/download/qq_27489007/19787322?spm=1001.2014.3001.5503" ref="nofollow noopener noreferrer">Unity粒子特效系列-下雨效果-毛毛细雨.zip-Unity3D文档类资源</a></p>
<h2 data-id="heading-7">👉后续</h2>
<p>这就完了？不存在的。</p>
<p><strong>小空还有下一篇，耶稣也改变不了。</strong></p>
<p><strong>我说的。</strong></p>
<p>新内容预览如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cd84884c8b1943baa74f6c43e7e6f325~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">​</p>
<h2 data-id="heading-8">👉其他</h2>
<blockquote>
<p>📢作者：小空和小芝中的小空</p>
<p>📢公众号：【空名先生】</p>
<p>📢转载说明：务必注明来源：<a href="https://juejin.cn/user/4265760844943479/columns" title="https://juejin.cn/user/4265760844943479/columns" target="_blank">芝麻粒儿 的个人主页 - 专栏 - 掘金 (juejin.cn)</a></p>
<p>📢欢迎点赞👍收藏🌟留言</p>
</blockquote>
<p>​</p></div>  
</div>
            