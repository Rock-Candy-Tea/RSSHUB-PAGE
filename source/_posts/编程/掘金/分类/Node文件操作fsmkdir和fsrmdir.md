
---
title: 'Node文件操作fs.mkdir和fs.rmdir'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9235b7a6db134ca5be88c62b852e9b63~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 21:36:24 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9235b7a6db134ca5be88c62b852e9b63~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">fs.mkdir文件目录新增</h2>
<h3 data-id="heading-1">案例使用</h3>
<ul>
<li>逐级新增目录 会成功打印success</li>
</ul>
<pre><code class="copyable">fs.mkdir("a", function (err) &#123;
    // 当a不存在的时候直接创建 a/b会报错
 if (err) &#123;
    console.log(err);
    return;
  &#125;
  console.log("success...");//success
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>跨级在不存在的目录下新增目录 报错啦！！，node本身的内置模块是不支持不存在的目录下新增目录的（这就是我要干的事）</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9235b7a6db134ca5be88c62b852e9b63~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">fs.mkdir的加强版</h3>
<h4 data-id="heading-3">递归版本</h4>
<ul>
<li>思路</li>
</ul>
<ol>
<li>对要新增的path路径根据"/"进行切割生成数组缓存</li>
<li>index 初始值= 1;对路径对应数组依次进行slice(0, index) 截取后join('/')成path字符串currentPath</li>
<li>fs.stat 用于描述文件的状态，如果不存在文件，就发生错误</li>
<li>上一天发生错误调用 fs.mkdir(currentPath, 递归调用自己);</li>
<li>文件存在调用自己</li>
</ol>
<ul>
<li>代码实现</li>
</ul>
<pre><code class="copyable">function mkdir(pathStr, cb) &#123;
  let pathList = pathStr.split("/");
  // 递归调用fs.mkdir
  let index = 1;
  function make(err) &#123;
    if (err) return cb(err);
    if (index === pathList.length + 1) return cb();
    //每次 调用要将上次的已经生成的文件名做下次的目标文件，
    // 所以 slice(0, index) 第二参数也要 累加
    //slice(0, index) 截取后join('/')  成字符串
    let currentPath = pathList.slice(0, index++).join("/");
    // console.log("pathList.slice(0,index)", pathList.slice(0, index));
    fs.stat(currentPath, function (err) &#123;
      if (err) &#123;
        fs.mkdir(currentPath, make);
        console.log(&#123; currentPath &#125;);
        // 如果不存在，再创建  fs.mkdir(currentPath, make);
      &#125; else &#123;
        make();
      &#125;
    &#125;);
  &#125;
  make();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>测试</li>
</ul>
<ol>
<li>此时已经不报错了</li>
</ol>
<pre><code class="copyable">mkdir("a/b/c/d", function (err) &#123;
  if (err) console.log(err);
   console.log("success...");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>打印效果</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26df12909220417a961e313e33b2ee77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ff9dba711604335a093691eb7cb74ec~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">for循环+await版本</h4>
<ul>
<li>实现思路</li>
</ul>
<ol>
<li>以‘/’为基准切割路径为对应数组，对数组进行for循环遍历</li>
<li>for循环里existsSync()以同步的方法检测目录是否存在。</li>
</ol>
<p>　　如果目录存在 返回 true ，如果目录不存在 返回false
3. 不存在 fs.mkdir(currentPath)</p>
<ul>
<li>实现代码</li>
</ul>
<pre><code class="copyable">const fs = require("fs").promises; //node11后可以直接.promises
const &#123; existsSync &#125; = require("fs");
async function mkdir(pathStr, cb) &#123;
  let pathList = pathStr.split("/");
  for (let i = 1; i <= pathList.length; i++) &#123;
    let currentPath = pathList.slice(0, i).join("/");
    if (!existsSync(currentPath)) &#123;
      await fs.mkdir(currentPath);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调用 将递归调用 平铺称then 链式调用</li>
</ul>
<pre><code class="copyable">mkdir("a/b/c/d")
  .then(() => &#123;
    console.log("创建成功");
  &#125;)
  .catch((err) => &#123;
    console.log(err);
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>打印效果</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f0730a81a484817b64a369d2bffe14b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae55dd8930ab4416b0e306147053b81d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">fs.rmdir文件目录删除</h2>
<h3 data-id="heading-6">案例使用</h3>
<ul>
<li>对存在子目录的目录直接进行fs.rmdir删除</li>
</ul>
<pre><code class="copyable">const fs = require("fs");
const path = require("path");
fs.rmdir("a", function (err) &#123;
  console.log(err);//会报错
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用结果（报错）</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bc0954d975645dc9babd8c20baa3d59~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">fs.rmdir加强版</h3>
<h4 data-id="heading-8">串行版本</h4>
<ul>
<li>思路</li>
</ul>
<ol>
<li>
<p>fs.stat 会返回文件的具体信息：文件的状态 文件的信息，修改时间，创建时间，目录状态；fs.stat 的回调里第二参数是获取到文件对象，对象的方法 ：isFile，isDirectory</p>
</li>
<li>
<p>isFile 直接  fs.unlink(dir, cb);删除当前文件</p>
</li>
<li>
<p>isDirectory 调用fs.readdir返回子目录组成的数组</p>
</li>
<li>
<p>对子目录数组进行map遍历&父文件名称+子文件名称拼接path.join(dir, item))</p>
</li>
<li>
<p>对拼接过的path数组依次进行递归调用自己</p>
</li>
<li>
<p>子目录全删除后删除本身</p>
</li>
</ol>
<ul>
<li>代码实现</li>
</ul>
<pre><code class="copyable">function rmdir(dir, cb) &#123;
  fs.stat(dir, function (err, statObj) &#123;
    // 1:判断dir的文件信息 statObj 是目录还是 文件
    if (statObj.isDirectory()) &#123;
      // 1.1 读取文件夹fs.readdir 回调函数 里可以拿到文件夹读取结果
      fs.readdir(dir, function (err, dirs) &#123;
        //   遍历 文件夹中文件，path 拼接 父文件名称+ 子文件名称
        dirs = dirs.map((item) => path.join(dir, item));
        // 把目录里面 的拿出来，一个删除后 删除下一个
        let index = 0;
        function step() &#123;
          // 将子文件都删除完后，删除自己
          if (index === dirs.length) return fs.rmdir(dir, cb);
          //删除第一个成功后 继续调用rmdir 删除下一个子文件，直到index===dirs.length 时 删除自己
          rmdir(dirs[index++], step);
        &#125;
        step();
      &#125;);
    &#125; else &#123;
      // 1.2 dir是文件 直接删除 用fs.unlink
      fs.unlink(dir, cb);
    &#125;
  &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>测试</li>
</ul>
<pre><code class="copyable">rmdir("a", function () &#123;
  console.log("删除成功");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行结果</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/530ed2b35d6b491b8ca1232f602ce542~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">并行版本</h4>
<ul>
<li>代码实现</li>
</ul>
<pre><code class="copyable">const fs = require("fs").promises;
const path = require("path");
async function rmdir(dir) &#123;
  let statObj = await fs.stat(dir);
  if (statObj.isDirectory) &#123;
    let dirs = await fs.readdir(dir);
    await Promise.all(dirs.map((item) => rmdir(path.join(dir, item))));
    await fs.rmdir(dir);
  &#125; else &#123;
    return fs.unlink(dir);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>调用</li>
</ul>
<pre><code class="copyable">rmdir("a").then(() => &#123;
  console.log("并行删除成功");
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>执行结果</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/de45815deec04e40804ce2d65c0304b6~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-10">并行和串行的区别</h4>
<p>串行 理解成单线程 要根据上一个执行结束后才能执行下一个
并行 异步执行 彼此之间无依赖关系
那么后者会比前者效率上更高效些些</p>
<h2 data-id="heading-11">文件目录的操作本质</h2>
<ol>
<li>文件目录本质：是树形结构数据</li>
<li>文件目录的操作是对树形结构的数据的操作</li>
<li>留个坑位 下次写<a href="https://juejin.cn/post/6975861599777062926/" target="_blank"> 树形结构的了解</a></li>
</ol>
<p><code>最后如果觉得本文有帮助 记得点赞三连哦 十分感谢</code></p></div>  
</div>
            