
---
title: 'Obsidian 随机生成读书笔记片段'
categories: 
 - 新媒体
 - 少数派 sspai
 - Matrix
headimg: 'https://cdn.sspai.com/2021/09/27/c66cc66b5326a2336306dbb65b9355ee.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
author: 少数派 sspai
comments: false
date: Mon, 27 Sep 2021 07:53:37 GMT
thumbnail: 'https://cdn.sspai.com/2021/09/27/c66cc66b5326a2336306dbb65b9355ee.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1'
---

<div>   
<div class="articleWidth-content" data-v-6a669db8><div class="content wangEditor-txt minHeight" data-v-6a669db8><p>现在阅读，以多看和微信读书为主，在阅读过程中会做笔记。一直想把这些笔记统一管理起来，标记出值得记忆的片段，每天随机生成，便于复习巩固。</p><p>Roam Research 有一个插件叫 Roam42，可以随机生成指定标签的笔记到新的笔记中，以便于复习。之前在推特上看 <a href="https://twitter.com/Tisoga">@Jiayuan</a> 就是用这种方式管理笔记的，非常羡慕这个功能。</p><p>后来经过摸索，发现 Dataview 可以在 Obsidian 中使用 JS 实现所有自己想要的效果，包括随机生成笔记复习这件事。我写了一个代码片段，可以随机生成 3 个带 <code>#Quote</code> 标签的读书笔记段落。</p><figure class="image ss-img-wrapper"><img src="https://cdn.sspai.com/2021/09/27/c66cc66b5326a2336306dbb65b9355ee.png?imageView2/2/w/1120/q/40/interlace/1/ignore-error/1" data-original="https://cdn.sspai.com/2021/09/27/c66cc66b5326a2336306dbb65b9355ee.png" referrerpolicy="no-referrer"></figure><p>具体代码块如下，<code>term</code> 表示标签名 <code>#Quote</code>，<code>ranNum</code> 表示随机数 3，可以根据自己的需要修改。将以下内容粘贴至笔记中，预览。拖动 Banner 可以再自动随机一次。</p><pre class="language-javascript"><code>```dataviewjs
//使用时修改关键词即可
const term = "#Quote"
const files = app.vault.getMarkdownFiles()
const arr = files.map(async ( file) => &#123;
const content = await app.vault.cachedRead(file)
const lines = content.split("\n").filter(line => line.contains(term))
return lines
&#125;)

function generateArray (start, end) &#123; return Array.from(new Array(end + 1).keys()).slice(start) &#125;

Promise.all(arr).then(values => &#123;
    //不包含本文件
    let noteArr = values.flat().filter(note => !note.includes("const term ="))
    //生成一个连续数值的数组
    let arrNum = generateArray(0,noteArr.length-1)
    let result = [ ]
    let ranNum = 3

    for (let i = 0; i < ranNum; i++) &#123;
        var ran = Math.floor(Math.random() * (arrNum.length - i))
        result.push(arrNum[ran])
        arrNum[ran] = arrNum[arrNum.length - i - 1]
    &#125;

    for(let i=0; i< result.length;i++)&#123;
        let j = result[i]
        dv.paragraph(`$&#123;noteArr[j]&#125;`)
    &#125;
&#125;)</code></pre><p>其他更多更详细的功能可以看知乎上的一个全面解读 <a href="https://zhuanlan.zhihu.com/p/373623264">Dataview 编写的教程</a> 。</p><blockquote><p>说明：本文同步发表于<a href="http://www.uncoverman.com/random-notes-in-obsidian.html" target="_blank">个人博客</a>。</p></blockquote></div><!----></div><div style="border:1px solid transparent;" data-v-6a669db8></div><div class="article-side sideTop" style="display:none;left:0;" data-v-7be936cf data-v-6a669db8><div class="download-guide-container" data-v-14f9065e data-v-7be936cf><div class="btn-wrapper" data-v-14f9065e><!----><button class="btn btn-view" data-v-14f9065e><i class="iconfont iconfont-phone" data-v-14f9065e></i></button></div><a href="https://sspai.com/s/JYjP" target="_blank" data-v-14f9065e><!----></a></div><div class="item-wrapper" data-v-7be936cf><button class="btn btn-charge" data-v-7be936cf><i class="iconfont" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>9</span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-comment" data-v-7be936cf><i class="iconfont iconfont-comment" data-v-7be936cf></i></button><span class="count" data-v-7be936cf>9</span></div><div class="item-wrapper" data-v-7be936cf><span data-v-7be936cf><div role="tooltip" id="el-popover-2670" aria-hidden="true" class="el-popover el-popper popper-share right ss-popper-dark-border" style="width:undefinedpx;display:none;"><!----><div class="article-side-share-btn"><a href="https://service.weibo.com/share/share.php?url=null?ref=weibo&title=%E3%80%90Obsidian%20%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%E7%89%87%E6%AE%B5%E3%80%91RoamResearch%E6%9C%89%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%8F%ABRoam42%EF%BC%8C%E5%8F%AF%E4%BB%A5%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E6%8C%87%E5%AE%9A%E6%A0%87%E7%AD%BE%E7%9A%84%E7%AC%94%E8%AE%B0%E5%88%B0%E6%96%B0%E7%9A%84%E7%AC%94%E8%AE%B0%E4%B8%AD%EF%BC%8C%E4%BB%A5%E4%BE%BF%E4%BA%8E%E5%A4%8D%E4%B9%A0%E3%80%82%E4%B9%8B%E5%89%8D%E5%9C%A8%E6%8E%A8%E7%89%B9%E4%B8%8A%E7%9C%8B%40Jiayuan%E5%B0%B1%E6%98%AF%E7%94%A8%E8%BF%99%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&pic=https%3A%2F%2Fcdn.sspai.com%2F2021%2F09%2F29%2Fcaf87c7884f7bc00e6561049838787a5.png%3FimageMogr2%2Fauto-orient%2Fquality%2F95%2Fthumbnail%2F!1420x708r%2Fgravity%2FCenter%2Fcrop%2F1420x708%2Finterlace%2F1&appkey=3196502474#" target="_blank"><i class="iconfont iconfont-weibo-simple right-16"></i></a><span><div role="tooltip" id="el-popover-6406" aria-hidden="true" class="el-popover el-popper" style="width:undefinedpx;display:none;"><!----><div style="text-align:center;"><div id="qr-code"></div><small class="qr-small">扫码分享</small></div></div><span class="el-popover__reference-wrapper"><i class="iconfont iconfont-wechat-simple right-16"></i></span></span><a href="https://twitter.com/share?text=%E3%80%90Obsidian%20%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E8%AF%BB%E4%B9%A6%E7%AC%94%E8%AE%B0%E7%89%87%E6%AE%B5%E3%80%91RoamResearch%E6%9C%89%E4%B8%80%E4%B8%AA%E6%8F%92%E4%BB%B6%E5%8F%ABRoam42%EF%BC%8C%E5%8F%AF%E4%BB%A5%E9%9A%8F%E6%9C%BA%E7%94%9F%E6%88%90%E6%8C%87%E5%AE%9A%E6%A0%87%E7%AD%BE%E7%9A%84%E7%AC%94%E8%AE%B0%E5%88%B0%E6%96%B0%E7%9A%84%E7%AC%94%E8%AE%B0%E4%B8%AD%EF%BC%8C%E4%BB%A5%E4%BE%BF%E4%BA%8E%E5%A4%8D%E4%B9%A0%E3%80%82%E4%B9%8B%E5%89%8D%E5%9C%A8%E6%8E%A8%E7%89%B9%E4%B8%8A%E7%9C%8B%40Jiayuan%E5%B0%B1%E6%98%AF%E7%94%A8%E8%BF%99%EF%BC%88%E6%9D%A5%E8%87%AA%20%40%E5%B0%91%E6%95%B0%E6%B4%BEsspai%EF%BC%89%E5%85%A8%E6%96%87%EF%BC%9A&url=null" target="_blank" class="twitter"><i class="iconfont iconfont-twitter-simple right-16"></i></a></div></div><span class="el-popover__reference-wrapper"><button class="btn-mini btn-share" data-v-7be936cf><i class="iconfont iconfont-share" data-v-7be936cf></i></button></span></span></div><div class="item-wrapper" data-v-7be936cf><button class="btn-mini btn-collect" data-v-7be936cf><i class="iconfont iconfont-collect" data-v-7be936cf></i></button></div><!----></div><!---->  
</div>
            