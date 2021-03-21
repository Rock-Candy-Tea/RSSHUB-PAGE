
---
title: MN3联动Anki：分享我修改的Marginnote3的Anki模板
categories: 
    - 学习
    - MarginNote - 标签
author: MarginNote - 标签
comments: false
date: Tue, 09 Mar 2021 03:52:04 GMT
thumbnail: https://bbs.marginnote.cn/uploads/default/optimized/2X/4/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941_2_690x434.png
---

<div>   
<blockquote>
<p>总体上仅在原来的基础上改动了CSS样式，作为核心的字段和正反面的代码没有修改，这样可以避免发生冲突。</p>
</blockquote>
<ol>
<li>
<p>调整了文本框宽度、字体大小、间距、行高，改动后呈现效果更适合大屏幕的电脑</p>
</li>
<li>
<p>改变了粗体、下划线、斜体的颜色</p>
</li>
<li>
<p>改变了cloze的颜色</p>
</li>
<li>
<p>为cloze加入了一个淡入动画（动画的代码参考了<a href="https://zhuanlan.zhihu.com/p/79679967" rel="nofollow noopener">知乎用户的文章</a>）</p>
</li>
</ol>
<blockquote>
<p>下面是改动前后的效果（内容参考书籍《为什么做个好人很难? 伦理学导论》）：</p>
</blockquote>
<p></p><div class="lightbox-wrapper"><a class="lightbox" href="https://bbs.marginnote.cn/uploads/default/original/2X/4/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941.png" data-download-href="https://bbs.marginnote.cn/uploads/default/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941" title="1.png"><img src="https://bbs.marginnote.cn/uploads/default/optimized/2X/4/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941_2_690x434.png" alt="1" data-base62-sha1="b640ndXyOuxokSEIPKKEQ4CBltL" width="690" height="434" srcset="https://bbs.marginnote.cn/uploads/default/optimized/2X/4/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941_2_690x434.png, https://bbs.marginnote.cn/uploads/default/optimized/2X/4/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941_2_1035x651.png 1.5x, https://bbs.marginnote.cn/uploads/default/optimized/2X/4/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941_2_1380x868.png 2x" data-small-upload="https://bbs.marginnote.cn/uploads/default/optimized/2X/4/4dc769c7ae9f7ded2c14e465c1cc3f22bb372941_2_10x10.png" referrerpolicy="no-referrer"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"/></svg><span class="filename">1.png</span><span class="informations">2682×1688 323 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"/></svg>
</div></a></div><p></p>
<p>我们可以看到MarginNote3默认的anki模板的 <strong>视觉效果在整体上有点瑕疵</strong> ，主要体现在：</p>
<ul>
<li>
<strong>字体、间距、行高偏小</strong> ：复习多张卡片会导致视觉疲劳</li>
<li>
<strong>边界适应屏幕而显得很宽</strong> ：对于大屏幕的电脑或平板等设备不友好</li>
<li>
<strong>Cloze（填空）的颜色是灰色</strong> ：无法快速地同普通字体区别开，视觉效果不够突出，每次复习卡片时需要花时间找到Cloze在哪里</li>
</ul>
<p></p><div class="lightbox-wrapper"><a class="lightbox" href="https://bbs.marginnote.cn/uploads/default/original/2X/4/466e6f03256239e5f45c77f9a86edca8b81cba7e.png" data-download-href="https://bbs.marginnote.cn/uploads/default/466e6f03256239e5f45c77f9a86edca8b81cba7e" title="2.png"><img src="https://bbs.marginnote.cn/uploads/default/optimized/2X/4/466e6f03256239e5f45c77f9a86edca8b81cba7e_2_665x500.png" alt="2" data-base62-sha1="a341BCUwhG4p5WBeevpr0TSPc3I" width="665" height="500" srcset="https://bbs.marginnote.cn/uploads/default/optimized/2X/4/466e6f03256239e5f45c77f9a86edca8b81cba7e_2_665x500.png, https://bbs.marginnote.cn/uploads/default/optimized/2X/4/466e6f03256239e5f45c77f9a86edca8b81cba7e_2_997x750.png 1.5x, https://bbs.marginnote.cn/uploads/default/optimized/2X/4/466e6f03256239e5f45c77f9a86edca8b81cba7e_2_1330x1000.png 2x" data-small-upload="https://bbs.marginnote.cn/uploads/default/optimized/2X/4/466e6f03256239e5f45c77f9a86edca8b81cba7e_2_10x10.png" referrerpolicy="no-referrer"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"/></svg><span class="filename">2.png</span><span class="informations">1870×1406 313 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"/></svg>
</div></a></div><p></p>
<ul>
<li>
<strong>改变色彩</strong> ：视觉焦点集中</li>
<li>
<strong>边界适中</strong> ：减少左右横扫的浏览压力</li>
</ul>
<blockquote>
<p>卡片模板的分享链接</p>
</blockquote>
<p><a href="https://pan.baidu.com/s/1LFxGjQtZuf5zoB68TO9D1Q" rel="nofollow noopener">https://pan.baidu.com/s/1LFxGjQtZuf5zoB68TO9D1Q</a>  密码:xhfp</p>
<blockquote>
<p>使用方法</p>
</blockquote>
<ol>
<li>
<p>MarginNote3摘录笔记</p>
</li>
<li>
<p>摘录笔记发送到MarginNote3内部的卡片组</p>
</li>
<li>
<p>在卡片组编辑界面进行挖空等调整</p>
</li>
<li>
<p>导出笔记到anki</p>
</li>
<li>
<p>因为MarginNote导出anki会自动覆盖现有模板，所以我把原本的MarginNote模板名字改成了<code>Marginnote3（夏暮）</code>，导出到anki后，在anki浏览器中全选导出的卡片笔记，右键更改笔记模板，改成我的这个即可。</p>
</li>
</ol>
          
</div>
            