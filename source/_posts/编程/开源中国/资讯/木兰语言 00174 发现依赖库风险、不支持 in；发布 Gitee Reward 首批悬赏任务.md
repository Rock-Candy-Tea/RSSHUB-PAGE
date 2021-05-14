
---
title: '木兰语言 0.0.17.4 发现依赖库风险、不支持 in；发布 Gitee Reward 首批悬赏任务'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3974'
author: 开源中国
comments: false
date: Fri, 14 May 2021 09:30:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3974'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <div> 
  <p>首先号外，刚在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2Fgitee_reward" target="_blank">Gitee Reward</a> 发布了首批三个总值 ￥916 的悬赏任务，走过路过莫错过：</p> 
  <ul> 
   <li>￥100 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3QHKV" target="_blank">【新人优先】重现一个内置函数——bytes</a></li> 
   <li>￥128 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3QHXU" target="_blank">【进阶】补完余下三十多个内置函数</a></li> 
   <li>￥688 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3QIEL" target="_blank">【老手】木兰源码转换为 Python</a></li> 
  </ul> 
  <h3>依赖库风险</h3> 
  <p>不知从何时开始，运行原始木兰的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2FMulanRevive%2Fmulan" target="_blank">逆向项目</a> 时，就会报 rply 警告 <code>ParserGeneratorWarning: Token '|=' is unused</code> 而且任何求值都报错 “IndexError: list index out of range”。</p> 
  <p>一直没细究，本周才发现是因为木兰语法中的 “|” （位或）操作符在 rply 0.7.8 中成为了保留字，详<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2FMulanRevive%2Fmulan-rework%2Fissues%2FI3QQ5O%253Ffrom%253Dproject-issue" target="_blank">见此 issue</a>，就是在今年一月 rply 发布了 0.7.8 后就有此问题。</p> 
  <p>具体说，木兰逆向中有 <code>@pg_.production('bin_expr : expr | expr')</code> 这一语法规则，也就是表达式的位或运算，而在 rply 0.7.8 中包含了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falex%2Frply%2Fpull%2F101" target="_blank">这个 PR</a>，将 | 作为语法规则的“或者”，也即 BNF 中 | 的原始语义。导致木兰的位或语法规则不能再识别。</p> 
  <p>为此问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falex%2Frply%2Fissues%2F100%2523issuecomment-836118708" target="_blank">跟帖</a> 尚未得到社区回应，想得到几种解决方案：</p> 
  <ul> 
   <li>限定用户安装 0.7.7 版本的 rply</li> 
   <li>向 rply 提 PR，通过转义等方法使语法规则重新支持 | 字符</li> 
   <li>另开 rply 分支并自行发布版本，可以回退问题 PR</li> 
  </ul> 
  <p>限定 rply 版本的问题是，0.7.7 并没有<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgithub.com%2Falex%2Frply%2Fcommit%2F6e16262dc6d434fc467eed83ed31ca764ba01a34" target="_blank">这个错误定位信息的修正</a>，影响调试和试用，如果两个 rply 版本在本机共存的话会增加开发测试的复杂度。</p> 
  <p>从之前的几次交流看，感觉 rply 社区已不大活跃，也许该早日考虑自行维护发布版本。</p> 
  <h3><code>__contains__</code> 代替 in</h3> 
  <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F190043049" target="_blank">去年挺早时候</a> 就发觉木兰不支持 Python 中的 in 关键词，一直没发现比 <code>__contains__</code> 更通用的变通办法，但还未死心。本周在重现 ast 生成木兰的这部分功能时，发现 Python 的 <code>'a' in d</code> 会被转换为木兰的 <code>(d.__contains__('a'))</code>，原可执行文件也确认了。看来在这个版本中，木兰并无更好的 in 替代语法。可惜！</p> 
  <p>类似地，Python 中的链式比较比如 <code>'a' in 'ab' in d</code>，会转换为木兰的“且”表达式 <code>('ab'.__contains__('a') and d.__contains__('ab'))</code>。个人感觉这个 Python 的链式语法并不像 in 那样常用，易用性问题似乎没那么大。</p> 
  <p><em><strong>最后，还请各位看看 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttps%253A%2F%2Fgitee.com%2Fgitee_reward" target="_blank">Gitee Reward</a> 悬赏榜，麻烦广而告之，多谢！</strong></em></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            