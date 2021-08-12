
---
title: '微信小程序中base64格式的小程序码通过canvas画出来无效'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4262'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 00:34:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=4262'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第4天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<h5 data-id="heading-0">使用场景</h5>
<p>小程序中的文章详情页面有一个分享功能：用户点击分享按钮，生成一张分享图片（包括封面图，简介以及带有文章ID的小程序码），方便用户保存在本地。</p>
<h5 data-id="heading-1">问题说明</h5>
<p>小程序码通过后台接口获取，格式如下：'data:image/jpg;base64,/9j/4AAQSkZJRgAB...'（只截取了前面一部分）</p>
<p>通过canvas画出来之后，在微信开发者工具上有效，在真机上无效。</p>
<h5 data-id="heading-2">解决方法</h5>
<p>先把小程序码通过小程序API中的FileSystemManager.writeFile()接口写入本地并获取到一个临时URL。</p>
<h5 data-id="heading-3">关键代码</h5>
<p>把小程序码写入本地</p>
<pre><code class="copyable">// 把小程序码写入本地
export const writeFile = (base64Str => &#123;
  return new Promise((resolve,reject)=>&#123;
    // 后台返回的base64格式数据的回车换行换为空字符''
    let base64Image =  base64Str.split(',')[1].replace(/[\r\n]/g, '');
    // 文件管理器
    const fsm = wx.getFileSystemManager();
    // 文件名
    const FILE_BASE_NAME = 'tmp_base64src';
    // 文件后缀
    const format = 'png';
    // 获取当前时间戳用于区分小程序码，防止多次写进的小程序码图片都一样，建议通过不同的列表ID来区分不同的小程序码
    const timestamp = (new Date()).getTime();
    // base转二进制
    const buffer = wx.base64ToArrayBuffer(base64Image),
    // 文件名
    filePath = `$&#123;wx.env.USER_DATA_PATH&#125;/$&#123;timestamp&#125;share.$&#123;format&#125;`;
    // 写文件
    fsm.writeFile(&#123;
      filePath,
      data: buffer,
      encoding: 'binary',
      success(res) &#123;
        // 读取图片
        wx.getImageInfo(&#123;
          src: filePath,
          success: function(res) &#123;
            let img = res.path;
            // 把需要画出来的图片的临时url暴露出去
            resolve(img);
            reject();
          &#125;,
          fail(e)&#123;
            console.log('读取图片报错');
            console.log(e);
          &#125;,
          error(res) &#123;
            console.log(res)
          &#125;
        &#125;)
      &#125;,
      fail(e)&#123;
        console.log(e);
      &#125;
    &#125;)
  &#125;).catch((e) => &#123;
    console.log(e);
  &#125;)
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在页面调用方法</p>
<pre><code class="copyable">
// 在页面调用方法
import &#123; writeFile &#125; from '../../utils/wxFunc'
 
getUseCode () &#123;
   writeFile(codeUrl).then(img => &#123; // // codeUrl为base64格式的小程序码
     console.log('可使用的小程序码：' + img); // img格式：http://usr/1599468897794share.png
     this.createCanvas(img);
   &#125;).catch(e => &#123;
     console.log(e);
   &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后还可以继续完善，这样每调用一次写一个文件，文件会越写越多，当文件管理器中文件总大小超过最大限制则会报错。解决方法：在写入文件之前先做一次删除操作。</p></div>  
</div>
            