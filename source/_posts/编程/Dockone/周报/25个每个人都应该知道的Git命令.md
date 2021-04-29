
---
title: '25个每个人都应该知道的Git命令'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=7916'
author: Dockone
comments: false
date: 2021-04-29 04:02:14
thumbnail: 'https://picsum.photos/400/300?random=7916'
---

<div>   
<br>我们大多数时候都使用IDE和其他软件来编写命令，但为了更好的工作，我们还需要随时准备一些可以随手使用的命令，以备不时之需。<br>
<br>以下是我在开发时候，通常使用的命令，今天，我将它分享与你，希望对你有所帮助。<br>
<h4><strong>1、初始化本地Git存储库</strong></h4><pre class="prettyprint">git init<br>
</pre><br>
<h4><strong>2、创建远程存储库的本地副本</strong></h4><pre class="prettyprint">git clone ssh://git@github.com/[username]/[repository-name].git<br>
</pre><br>
<h4><strong>3、检查状态</strong></h4><pre class="prettyprint">git status<br>
</pre><br>
<h4><strong>4、将文件添加到暂存区</strong></h4><pre class="prettyprint">git add [file-name.txt] <br>
</pre><br>
<h4><strong>5、将所有新文件和更改过的文件添加到登台区域</strong></h4><pre class="prettyprint">git add -A<br>
</pre><br>
<h4><strong>6、提交更改</strong></h4><pre class="prettyprint">git commit -m "[commit message]"<br>
</pre><br>
<h4><strong>7、删除文件（或文件夹）</strong></h4><pre class="prettyprint">git rm -r [file-name.txt]<br>
</pre><br>
<h4><strong>8、列出分支（星号表示当前分支）</strong></h4><pre class="prettyprint">git branch<br>
</pre><br>
<h4><strong>9、创建一个新分支</strong></h4><pre class="prettyprint">git branch [branch name] <br>
</pre><br>
<h4><strong>10、删除分支</strong></h4><pre class="prettyprint">git branch -d [branch name] <br>
</pre><br>
<h4><strong>11、创建一个新分支并切换到该分支</strong></h4><pre class="prettyprint">git checkout -b [branch name] <br>
</pre><br>
<h4><strong>12、克隆一个远程分支并切换到该分支</strong></h4><pre class="prettyprint">git checkout -b [branch name] origin/[branch name] <br>
</pre><br>
<h4><strong>13、重命名本地分支</strong></h4><pre class="prettyprint">git branch -m [old branch name] [new branch name] <br>
</pre><br>
<h4><strong>14、切换到分支</strong></h4><pre class="prettyprint">git checkout [branch name] <br>
</pre><br>
<h4><strong>15、将一个分支合并到活动分支中</strong></h4><pre class="prettyprint">git merge [branch name] <br>
</pre><br>
<h4><strong>16、将一个分支合并到一个目标分支</strong></h4><pre class="prettyprint">git merge [source branch] [target branch] <br>
</pre><br>
<h4><strong>17、将更改存储在不合适的工作目录中</strong></h4><pre class="prettyprint">git stash<br>
</pre><br>
<h4><strong>18、删除所有隐藏的条目</strong></h4><pre class="prettyprint">git stash clear<br>
</pre><br>
<h4><strong>19、将分支推送到你的远程存储库</strong></h4><pre class="prettyprint">git push origin [branch name] <br>
</pre><br>
<h4><strong>20、将更改推送到远程存储库</strong></h4><pre class="prettyprint">git push<br>
</pre><br>
<h4><strong>21、将本地存储库更新为最新的提交</strong></h4><pre class="prettyprint">git pull<br>
</pre><br>
<h4><strong>22、从远程存储库中提取更改</strong></h4><pre class="prettyprint">git pull origin [branch name] <br>
</pre><br>
<h4><strong>23、添加一个远程存储库</strong></h4><pre class="prettyprint">git remote add origin ssh://git@github.com/[username]/[repository-name].git<br>
</pre><br>
<h4><strong>24、查看更改</strong></h4><pre class="prettyprint">git log<br>
</pre><br>
<h4><strong>25、合并前预览更改</strong></h4><pre class="prettyprint">git diff [source branch] [target branch] <br>
</pre><br>
<h3><strong>结论</strong></h3>希望本指南内容对你有所帮助。还有其他我们错过的命令吗？如果是这样，请在评论中让我知道！<br>
<br>原文链接：<a href="https://mp.weixin.qq.com/s/rZHeVUdW6o_XjKlFKYC-pw" rel="nofollow" target="_blank">https://mp.weixin.qq.com/s/rZHeVUdW6o_XjKlFKYC-pw</a>
                                
                                                              
</div>
            