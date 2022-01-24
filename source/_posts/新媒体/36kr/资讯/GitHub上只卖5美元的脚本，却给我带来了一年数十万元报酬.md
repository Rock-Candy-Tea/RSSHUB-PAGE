
---
title: 'GitHub上只卖5美元的脚本，却给我带来了一年数十万元报酬'
categories: 
 - 新媒体
 - 36kr
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9891'
author: 36kr
comments: false
date: Mon, 24 Jan 2022 06:50:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=9891'
---

<div>   
<p>“一年多之前我把工作‘自动化’了，没有告诉任何人。”</p> 
<p>日前 Reddit 一个关于“利用自动化程序完成工作”的帖子迅速走红，收获八万多个赞，以及超 5000 条评论。作者是一名服务于律所的程序员，他通过脚本程序将自己的工作变成自动化处理，于是每天只需工作 10 分钟，就能赚取“接近 9 万（美元）”的年薪，他在帖子中简要分享了自己的工作。</p> 
<h2 label="一级标题" style>每天只在办公桌前待 10 分钟 </h2> 
<p>根据帖子，该程序员受雇于一家中等规模的律师事务所，职位是 IT 专家，主要处理所有用于审判的电子证据。目前律所正在将证据管理系统更改为基于云的系统，并希望这名程序员是唯一拥有云管理员访问权限的人，其他人只有查看权限并在<a class="project-link" data-id="162448" data-name="本地网" data-logo="https://img.36krcdn.com/20210808/v2_6908df955fdf4430afd567f60eb31b87_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/162448" target="_blank">本地网</a>络驱动器上工作。</p> 
<p>问题是，律所给的这唯一任务并不需要 8 小时来完成，于是在新冠肺炎疫情之前，这位 IT 专家大部分时间都被“困”在办公室里假装工作，而疫情发生后，远程工作模式开启，“摸鱼”空间就大幅增加了。</p> 
<p>他花了约一周时间，编写、调试和完善一个简单的脚本去完成自己的工作。这个脚本扫描本地驱动器来查找新的文件，为它们生成哈希值，将它们传输到云上，然后再次生成哈希值以确保真实性（在法庭上，必须证<a class="project-link" data-id="518491" data-name="明电" data-logo="https://img.36krcdn.com/20210813/v2_748bc6197d0746dd824c06d512d49593_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/518491" target="_blank">明电</a>子证据没有被篡改）。然后，他只需每天打卡上班，其<a class="project-link" data-id="523130" data-name="他时" data-logo="https://img.36krcdn.com/20210813/v2_d573e244a89c4b0ba1c0743a4d21873c_img_000" data-refer-type="2" href="https://36kr.com/projectDetails/523130" target="_blank">他时</a>间就玩玩游戏或想做什么就做什么，下班的时候检查日志以确保一切顺利，然后打卡下班。</p> 
<p>如此一来，实际上他每天只在办公桌前待 10 分钟。“有一段时间我感到内疚，好像有种在敲诈律师事务所的感觉，但最终我说服自己，只要每个人都开心，就没有伤害。我正在做他们雇我做的事，所有的工作都按时完成，我开始享受我的生活。”</p> 
<h2 label="一级标题" style>怎么做到的？ </h2> 
<p>在贴子发出后的这十多天内，作者更新了 2 次帖子，以回复网友问得最多的问题，比如，报酬是多少？答案是近 9 万美元。</p> 
<p>还比如，为什么律所会认为这是一份需要每天用 8 小时处理的工作？他回答道：“在他们雇用我之前，他们一直在努力跟上事情的发展。员工在一天结束时提交他们放置在本地驱动器上的所有文件的电子表格。然后管理员将检查电子表格并手动将文件夹 / 文件拖放到云端。我仍然每天都会收到电子表格，用它来验证我的日志。”</p> 
<p>虽然有人觉得作者这是懒惰、甚至在浪费生命，但他不觉得自己是这样的人，他说自己另外有做一个出于热情的项目，而不是说白天就只躺着玩游戏。</p> 
<p>那又为什么感到内疚呢，作者回答说也许是因为这些人都是律师。“我不讨厌我的老板。他实际上非常好，尽管根本不精通技术。我实际上并没有与律师<a class="project-link" data-id="81906" data-name="一起" data-logo="https://img.36krcdn.com/20210709/v2_647b9860d6f7437caf1be2501d37698a_img_000" data-refer-type="1" href="https://www.36dianping.com/space/4772100123" target="_blank">一起</a>工作或见律师，我属于行政管理，因为他们没有 IT 部门。”</p> 
<p>至于使用什么代码语言，以及怎么能做到这一点？作者回复道，“部分批处理文件执行用的 PowerShell 脚本。基本代码非常简单，其中大部分来自<a class="project-link" data-id="3968996" data-name="谷歌" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968996" target="_blank">谷歌</a>搜索‘批处理文件传输’（.bat transfer files）之类的内容，例如‘如何批处理传输某些类型的文件’等等。诀窍在于让脚本能适用于我们办公室，知道在哪里扫描新的文件，知道哪里是因为滞后而不能扫描的位置（讲真，如果你有一个包含 200000 个 .txt 文件的文件夹，那么一些垃圾会大大降低扫描速度。这时候最好手动操作，然后更改脚本以在以后的搜索中忽略该文件夹。）”</p> 
<p>有人问作者为什么不卖掉脚本然后大赚一笔，他坦言这不是价值数百万美元的高端程序。这是用记事本编写的几行代码。它目前在这所律所里发挥价值，是因为这里的人都没有技术技能，“这只能放在 GitHub 上然后卖个 5 美元。”</p> 
<p>另外，有网友质疑其真实性，因为觉得“不可能这么简单”。对此，作者回应称确实没那么简单——“脚本中涉及更多步骤，它执行我没有在这里讨论的功能。讨论这些功能更有可能泄露我的坐标。但脚本的核心，传输和哈希等等都是真实的。而所采取的针对我所在办公室的额外步骤的内容，我都省略了。”</p> 
<h2 label="一级标题" style>当你用程序代替自己工作，需要告诉老板吗？ </h2> 
<p>在律所程序员的帖子下面，有 Reddit 用户提到通过程序自动化工作是个趋势，并可能会影响他们的下一个就业决定。“我觉得所有这些类型的帖子教会我的是我需要 1)学习如何编码和 2) 找到一份悠闲的办公室工作。”</p> 
<p>获得最多赞同的第一热评则说，“将你的工资看成是自动化程序的订阅服务，哈哈。大公司都喜欢订阅服务吧。”</p> 
<p>但也正如帖子里提到的，近年来，类似的例子并不少见。2016 年 Reddit 上也有一个程序员分享说自己在过去 6 年内实际工作时间可能只有 50 个小时，因为入职 8 个月后就把全部工作自动化了。第六年老板意识到这个事情后，就把他解雇了。最终主角不仅删除了分享帖，也删除了整个账户。</p> 
<p>大概一年后，又一个名为 Etherable 的人在 Stack Exchange 上提了一个问题: “我不告诉我的雇主我的工作已经自动化了，这是不是不道德? ”——这位程序员接受了一份“美化数据录入”的工作，并且 6 个月前编写了脚本让工作可以自动化处理，原本 1 个人需要 1 个月完成的工作，最后变成只需 10 分钟。这份工作是全职且有福利，也允许 Etherable 在家办公。但 Etherable 隐约觉得自己做得不太对，他每隔一周就告诉公司自己完成部分工作，甚至会特意在里面加入少量错误，然后让同事测试，以让工作看起来更像是人工处理的。总的来说他每星期只需要工作一两个小时，但领的是全职薪酬。</p> 
<p>当时评论如潮，但呈现两极化，有认为 Etherable 出售的不是每星期 40 小时的数据输入工作，而是“处理 X 张试算表”的结果，因此以自动化程序处理并非不道德，但刻意加入错误去掩饰这是不诚实的行为，有可能会损害公司利益，因此可以不必告诉公司自动化程序的事情，但不能不诚实。</p> 
<p>而持相反意见的则认为 Etherable 只工作一两小时却收了 40 小时的薪水，每星期都谎报自己完成的工作，刻意加入错误欺骗公司并令同事还要花时间确认其工作等等，这已经是不道德的行为。</p> 
<p>相比之下，Etherable 的例子似乎会复杂些，因为他还有刻意犯错的行为。不过本质上，不管是 Etherable 还是其他人，这些将工作自动化的程序员或许更想知道的是：如何确保自己的饭碗安全？</p> 
<p><strong>参考链接：</strong></p> 
<p>https://old.reddit.com/r/antiwork/comments/s2igq9/i_automated_my_job_over_a_year_ago_and_havent/</p> 
<p>https://getpocket.com/explore/item/the-coders-programming-themselves-out-of-a-job?utm_source=wanqu.co&utm_campaign=Wanqu+Daily&utm_medium=website</p> 
<p class="editor-note">本文来自<a class="project-link" data-id="3968527" data-name="微信" data-logo="https://img.36krcdn.com/20200916/v2_811751a081924fa9af8741ce120bd7bf_img_png" data-refer-type="2" href="https://36kr.com/projectDetails/3968527" target="_blank">微信</a>公众号<a target="_blank" rel="noopener noreferrer nofollow" href="https://mp.weixin.qq.com/s/cGjyGbhQhLfMSMmF9IPGbg">“InfoQ”（ID:infoqchina）</a>，作者：燕珊，36氪经授权发布。</p>  
</div>
            