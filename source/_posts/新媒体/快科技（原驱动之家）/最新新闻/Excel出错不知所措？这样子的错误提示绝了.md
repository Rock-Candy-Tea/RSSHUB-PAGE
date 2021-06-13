
---
title: 'Excel出错不知所措？这样子的错误提示绝了'
categories: 
 - 新媒体
 - 快科技（原驱动之家）
 - 最新新闻
headimg: 'https://img1.mydrivers.com/img/20210613/b2781d1f5ff44a7c8b999585e4c52a39.gif'
author: 快科技（原驱动之家）
comments: false
date: Sun, 13 Jun 2021 08:42:47 GMT
thumbnail: 'https://img1.mydrivers.com/img/20210613/b2781d1f5ff44a7c8b999585e4c52a39.gif'
---

<div>   
<p>公式出错，大概是最令表哥表姐们头疼的一件事了。当然也分两种：一是公式本身就有错误，这时主要依赖于排错解决。另一种情况，则是公式本身没错，但由于原始数据等方面的缘故，不可避免产生了一些与期望值不符的结果。那么要想解决后一种情况，一般都有哪些方法呢？</p>
<p><strong>1、IFERROR 函数</strong></p>
<p>从函数的名称也能看出，这家伙其实就是专为公式出错而设计的。简单来说，它的使用只需要两组变量，“判断哪个单元格出错”以及“出错后显示什么？”。举个例子，当我们要制作一份考勤表时，通常会使用“实际出勤数 / 应该出勤数”来求取“出勤率”。但这里往往会涉及一个问题，即当“应该出勤数”还未填写时，单元格就会弹出一个“除零错误”（#DIV/0!）。</p>
<p align="center"><img alt="Excel出错不知所措？这样子的错误提示绝了" h="414" src="https://img1.mydrivers.com/img/20210613/b2781d1f5ff44a7c8b999585e4c52a39.gif" style="border: black 1px solid;" w="382" referrerpolicy="no-referrer"><br>
▲用 IFERROR 函数解决原始数据出错</p>
<p>解决这个问题的方法很多，比如先通过 IF 函数做个判断，如果“应该出勤数”已经填写，就按规则计算，如果尚未填写，就先显示个“0”占个坑。</p>
<p>不过你也看到了，这个方法很笨，而且会把公式变得冗长。相比之下，IFERROR 只要告诉它出错后，应该显示什么就可以了（本例即出错时显示“空白”，不出错按原公式计算），既简单又轻便。</p>
<p align="center"><img alt="Excel出错不知所措？这样子的错误提示绝了" h="414" src="https://img1.mydrivers.com/img/20210613/30c8cad4835d47f6bfb126df48b17fe3.gif" style="border: black 1px solid;" w="382" referrerpolicy="no-referrer"><br>
▲自定义出错提示词</p>
<p>此外你也可以通过修改 IFERROR 后面的“出错值”，来实现一些更“人性化”的提示。比如当数据出错时，显示“还没数据呢”（记得提示文字一定要用引号括起来）等等。总之方法到位了，怎么喜欢就怎么来吧！</p>
<p><strong>2、“0”值处理</strong></p>
<p>除了单独的出错提示外，有时我们也会看到一大堆“0”值。这个原因其实和上文差不多，也是由于原始数据未填写（更新）所致。不过由于不是出错提示，IFERROR 在这里已经不起作用，我们需要更换一个思路。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210613/e9b556a8-57d8-4f57-bbb0-a67f3e8cd1c8.jpg" target="_blank"><img alt="Excel出错不知所措？这样子的错误提示绝了" h="486" src="https://img1.mydrivers.com/img/20210613/Se9b556a8-57d8-4f57-bbb0-a67f3e8cd1c8.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
▲取消“在具有零值的单元格中显示零”勾选</p>
<p>点击“文件”→“选项”→“高级”，将右面板的进度条下拉，取消“在具有零值的单元格中显示零”前面的勾选，就能在 Excel 中禁止“0”的显示。</p>
<p>不过和 IFERROR 仅处理出错公式不同，“禁零法”则会连带着将正常的“0”值禁用。因此在使用这个方法时，需要更为谨慎一点。</p>
<p><strong>3、数据验证</strong></p>
<p>对于某些容易输错的字段（比如身份证号），我们通常会使用“数据有效性”加以控制。一般来说，如果所输的内容不合规，就会弹出一个“此值与此单元格定义的数据验证限制不匹配”的提示。没错！这个提示很微软。</p>
<p style="text-align: center"><a href="https://img1.mydrivers.com/img/20210613/4b5a8c1b-767c-4f3d-85bd-27d96e31ab3a.jpg" target="_blank"><img alt="Excel出错不知所措？这样子的错误提示绝了" h="585" src="https://img1.mydrivers.com/img/20210613/S4b5a8c1b-767c-4f3d-85bd-27d96e31ab3a.jpg" style="border: black 1px solid" w="600" referrerpolicy="no-referrer"></a><br>
▲修改出错提示文字</p>
<p>能不能让提示文字更易懂一点呢？很简单，只要在设置数据有效性时，点击旁边的“出错警告”，然后再把你琢磨好的提示文字输入进去即可。这样当输入内容不符合规范时，我们至少能看到一个能看懂的提示了。</p>
<p style="text-align: center"><img alt="Excel出错不知所措？这样子的错误提示绝了" h="173" src="https://img1.mydrivers.com/img/20210613/43c70446-c0fd-43da-ad32-7af82afdbf23.jpg" style="border: black 1px solid" w="414" referrerpolicy="no-referrer"><br>
▲修改后的出错提示</p>
<p><strong>4、重复输入提醒</strong></p>
<p>除了上面这些后知后觉的提醒以外，我们也可以对一些重复录入进行限制。实现这一功能同样也要借助“数据有效性”，只不过重点是将“验证条件”改为“自定义”，并在公式栏中输入“=COUNTIF (B:B,B1)=1”。</p>
<p>这段公式的作用，是当 B 列中出现重复数据时（即 COUNTIF 值 > 1），停止录入并弹出提示。当然你也可以借助上文那个方法，对这个提示自定义一下。</p>
<p align="center"><img alt="Excel出错不知所措？这样子的错误提示绝了" h="736" src="https://img1.mydrivers.com/img/20210613/aea95c501bf04378807e02ac5e33696b.gif" style="border: 1px solid black; width: 600px;" w="700" referrerpolicy="no-referrer"><br>
▲通过“数据有效性”防止重复录入</p>
<p><strong>写在最后</strong></p>
<p>以上四种方法是平时最常用的，基本上可以涵盖掉日常使用的方方面面。其实出错本身并不可怕，真正可怕的是明明出了错，却没有任何提醒。好了，以上就是本期要和大家分享的几个小技巧，喜欢的话就点个赞吧！</p>

           
           
<p class="end"> - THE END -</p> 
            
 <p class="bqian"><a href="https://news.mydrivers.com/tag/excel.htm"><i>#</i>Excel</a></p>
<p class="url">
     <span>原文链接：<a href="https://pcedu.pconline.com.cn/1426/14266487.html#ad=6883">太平洋电脑网</a></span>
<span>责任编辑：随心</span>
</p>
        
</div>
            