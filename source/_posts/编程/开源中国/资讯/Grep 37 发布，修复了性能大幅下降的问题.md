
---
title: 'Grep 3.7 发布，修复了性能大幅下降的问题'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5302'
author: 开源中国
comments: false
date: Tue, 17 Aug 2021 06:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5302'
---

<div>   
<div class="content">
                                                                                            <p>GNU Grep 被程序员、系统管理员和其他开发者广泛使用，用于从命令行搜索文本数据。Grep 3.7 的发布主要是为了修复困扰 Grep 的 "性能大幅下降" 问题。</p> 
<p>在 Grep 3.6 之后的 40 周内，有 6 位开发者进行了 33 次代码提交。在 Grep 3.7 版中值得注意的变化包括：</p> 
<p>行为上的改变：</p> 
<ul> 
 <li>使用 <code>--unix-byte-offsets</code> (-u) 选项现在会引起一个警告。自 3.1 以来，这个仅适用于 Windows 的选项没有任何影响。</li> 
</ul> 
<p>错误修复：</p> 
<ul> 
 <li>当太多的模式被散列到太少的 buckets 中时，预处理 N 个模式至少需要 O(N^2) 的时间。现在这只需要几秒钟，而不是此前所需的几天时间。</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsavannah.gnu.org%2Fforum%2Fforum.php%3Fforum_id%3D10037" target="_blank">https://savannah.gnu.org/forum/forum.php?forum_id=10037</a></p>
                                        </div>
                                      
</div>
            