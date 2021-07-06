
---
title: '带你用VUE实现上传图片效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d059bf2e03394c04a3c21977a0cd5dfd~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 18:04:50 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d059bf2e03394c04a3c21977a0cd5dfd~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>​摘要：在逛 b 站时看到一个上传图片的效果，想着可以自己也做一个，因为原作者是用原生 js 写的，那我不如就用 vue 写好了，当然，是一个很小的东西，在 HTML 文件直接引用 vue 就好了，详细步骤如下~</p>
</blockquote>
<p>本文分享自华为云社区<a href="https://bbs.huaweicloud.com/blogs/281564?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">《vue实现上传图片并预览效果》</a>，原文作者：北极光之夜。 。</p>
<h2 data-id="heading-0">一、话不多说，先看效果：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d059bf2e03394c04a3c21977a0cd5dfd~tplv-k3u1fbpfcp-zoom-1.image" alt="带你用VUE实现上传图片效果" loading="lazy" referrerpolicy="no-referrer">大家好，(๑╹◡╹)ﾉ” 这是我在逛 b 站时看到一个上传图片的效果，想着可以自己也做一个，因为原作者是用原生 js 写的，那我不如就用 vue 写好了，当然，是一个很小的东西，在 HTML 文件直接引用 vue 就好了，详细步骤如下~</p>
<h2 data-id="heading-1">二、详细实现步骤：</h2>
<h3 data-id="heading-2">1、先定义基本标签：</h3>
<p>先不管标签里面的 vue 指令，先定义基本 HTML 标签。</p>
<pre><code class="copyable"><div id="app">
         <div class="upload">           
           <input type="file" id="file" multiple @change="upload">
         </div>
        <ul class="view">
            <li>
                <img src="./img/52.jpg">
                <div class="delect" title="删不了我" @click="noDelect">×</div>
            </li>
            <li v-for="(item,index) in list" :key="index" >
                <img :src="item">
                <div class="delect" @click="delect(index)">×</div>
            </li>     
        </ul>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>.upload 是上传图片盒子，里面有一个 input 类型为 file 的标签；</p>
<p>.view 是放图片的大盒子，每个小 li 是一张图片，默认有一张图，还有一个小 li 是为了 v-for 渲染的；</p>
<p>delect 是删除图片按钮；</p>
<h3 data-id="heading-3">2、开始定义基本 css 样式：</h3>
<p>此为全局与底层盒子样式。</p>
<pre><code class="copyable"> *&#123;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        &#125;
        #app&#123;
            width: 900px;
            background-color: rgb(241, 241, 241);
            margin: 50px auto;
        &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">3、 .view 的样式：</h3>
<pre><code class="copyable"> .view&#123;
           display: flex;
           justify-content: space-around;
           flex-wrap: wrap;
           align-items: space-around;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>display: flex;flex 布局；</p>
<p>justify-content：space-around；主轴每个子项目间隔对齐。</p>
<p>flex-warp：warp；换行。</p>
<p>align-items：space-around：交叉轴每个子项目间隔对齐。</p>
<h3 data-id="heading-5">4、 图片的样式：</h3>
<pre><code class="copyable"> .view > li&#123;
            width: 200px;
            height: 120px;
            background-color: rgba(54, 194, 35,0.1);
            list-style: none;
            margin: 20px;
            position: relative;
        &#125;
        .view > li > img&#123;
            width: 100%;
            height: 100%;
            object-fit: cover;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>object-fit：cover； 图片保持原有比例，不拉伸。</p>
<h3 data-id="heading-6">5、 .deldect 按钮的样式：</h3>
<pre><code class="copyable"> .delect&#123;
            position: absolute;
            right: 0;
            top: 0;
             width: 20px;
             height: 20px;
             text-align: center;
             line-height: 20px;
             font-size: 15px;
             background-color: rgba(255, 255, 255,0.5);
             user-select: none;
             cursor: pointer;
             opacity: 0;
        &#125;
        .delect:hover&#123;
            
            background-color: rgba(31, 31, 31, 0.5);
             color: white;
        &#125;
        .view>li:hover .delect&#123;
            opacity: 1;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>user-select:none; 文本不可选中；</p>
<p>opacity：0； 透明度；</p>
<h3 data-id="heading-7">6、更改 input 标签的样式：</h3>
<p>通过在 input 标签外套一个 div，把 input 标签设为透明，然后给 div 设置想要的样式。可给 div 设置一个双伪类元素，填上文字与样式。</p>
<pre><code class="copyable"> .upload&#123;
            width: 80px;
            height: 20px;
            background-color: rgba(135, 206, 235,0.2);
            border: 1px dashed black;
            border-radius: 5px;
            position: relative;
        
        &#125;
        .upload:hover&#123;
            background-color: rgba(135, 206, 235,1);
        &#125;
        .upload::before&#123;
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            content: '上传图片';
            font-size: 13px;
            text-align: center;
            font-family: 'fangsong';
            line-height: 20px;
            user-select: none;
        &#125;
        #file&#123;
            width: 100%;
            height: 100%;
            opacity: 0;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">7、给我们的单页面引入 vue 和声明 vue 实例对象：</h3>
<pre><code class="copyable"> <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
          var app = new Vue(&#123;
              el:"#app",
              data: &#123;&#125;,
              methods: &#123;&#125;
          &#125;)     
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">8、给 input 标签绑定一个 change 事件，同时声明一个 list 数组：</h3>
<p>list 数组会存放每张图的地址。</p>
<pre><code class="copyable"> <input type="file" id="file" multiple @change="upload">
  data: &#123;
            list:[]
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">9、 定义 upload 方法，实现把选择的全部图片地址存放到 list 数组：</h3>
<p>upload 函数在 methods：&#123; &#125; 里声明。</p>
<pre><code class="copyable">   upload(e)&#123;
       //e.target指向事件执行时鼠标所点击区域的那个元素，那么为input的标签，
      // 可以输出 e.target.files 看看，这个files对象保存着选中的所有的图片的信息。
                      console.log(e.target.files)
                 //------------------------------------------------------     
                   // 既然如此，循环这个files对象，用for of 循环，     
                      for(let item of e.target.files)&#123;
                      //正则表达式，判断每个元素的type属性是否为图片形式，如图
                        if (!/image\/\w+/.test(item.type)) &#123;
                            // 提示只能是图片，return
                                alert("只能选择图片");
                                return;
             &#125; 
             // 保存下当前 this ，就是vue实例
                            var _this = this;
                       //  创建一个FileReader()对象，它里面有个readAsDataURL方法
                            let reader = new FileReader();
                            // readAsDataURL方法可以将上传的图片格式转为base64,然后在存入到图片路径, 
                            //这样就可以上传电脑任意位置的图片                            
                            reader.readAsDataURL(item);
                            //文件读取成功完成时触发
                            reader.addEventListener('load',function()&#123;
                            //  reader.result返回文件的内容。
                            //只有在读取操作完成后，此属性才有效，返回的数据的格式取决于是使用哪种读取方法来执行读取操作的。
                                //给数组添加这个文件也就是图片的内容
                                _this.list.push(this.result)
                            &#125;)
                    &#125;
                 //------------------------------------------------------------
                 &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbcb073a739d41cf8e22417af7e13bb6~tplv-k3u1fbpfcp-zoom-1.image" alt="带你用VUE实现上传图片效果" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">10、页面显示数组的每张图片：</h3>
<pre><code class="copyable"> <li v-for="(item,index) in list" :key="index" >
                <img :src="item">
                <div class="delect" @click="delect(index)">×</div>
            </li>    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>给小 li 绑定 v-for 循环，循环 list 数组，每个元素其实就是一个地址，绑定到图片的 src 属性上。index 是给数组的每个元素设置一个索引值。可以理解成数组下标嘛。</p>
<h3 data-id="heading-12">11、定义删除图片的方法：</h3>
<p>先给做删除的盒子绑定一个点击事件，同时传入 index 索引值，好知道是点击了哪张图：</p>
<pre><code class="copyable"> <div class="delect" @click="delect(index)">×</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>用 splice 方法删除 list 数组里对应的数据就好。</p>
<pre><code class="copyable">delect(index)&#123;
                     console.log(index);
                     this.list.splice(index,1);                    
                 &#125;,
                 // 这是默认图片的方法，弹出默认图片无法删除
                 noDelect()&#123;
                     alert('默认图片无法删除。')
                 &#125;
              &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-13">三、源码分享：</h2>
<p>**下载地址如下：**<a href="https://gitee.com/aurora-in-winter/blog/tree/master/" target="_blank" rel="nofollow noopener noreferrer">gitee.com/aurora-in-w…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30f26afe541e4b08ac085774e72ee027~tplv-k3u1fbpfcp-zoom-1.image" alt="带你用VUE实现上传图片效果" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://bbs.huaweicloud.com/blogs?utm_source=juejin&utm_medium=bbs-ex&utm_campaign=other&utm_content=content" target="_blank" rel="nofollow noopener noreferrer">点击关注，第一时间了解华为云新鲜技术~</a></p></div>  
</div>
            