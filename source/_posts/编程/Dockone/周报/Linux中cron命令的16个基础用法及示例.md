
---
title: 'Linux中cron命令的16个基础用法及示例'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=8904'
author: Dockone
comments: false
date: 2021-09-14 06:10:05
thumbnail: 'https://picsum.photos/400/300?random=8904'
---

<div>   
<br>Linux/Unix中，我们可以使用<code class="prettyprint">cron</code>命令自动运行和计划任务，你可以一次或定期执行任务。“Cron”广泛用于定期执行重复性工作（使用名为“crontab”的命令运行），“at”程序用于在特定时间段内执行一次任务。Crontab为所有用户维护单独的crontab文件。这些自动化的工作对许多使用Linux服务器的管理员来说是非常有用的。<br>
<br>一般来说，“crontab”文件用于备份、更新系统、同步服务器等任务。cron的一个重要优点是，你不需要详细了解它，只需要知道如何使用它作为设置cron作业的一部分。<br>
<br>本教程将指导你使用crontab的各种选项。下文中所有crontab的例子都在RHEL/CENTOS 7.6上测试过。<br>
<br>首先，让我们看看crontab的基本语法和表达式：<br>
<pre class="prettyprint">Minute hour Day-of-Month Month-of-Year Day-of-Week Command<br>
0-59 0-23 1-31 1-12 0-6 command / script<br>
</pre><br>
Crontab总共有6个字段。第1-5个字段是日期和时间，第6个字段可用于任何可执行的Linux命令或脚本。<br>
<br>注意：时间字段采用24小时格式。<br>
<h4>1. 如何在每天的特定时间执行cronjob？</h4>要把任务添加到crontab中，我们应该使用<code class="prettyprint">'-e'</code>选项。一旦添加了任务，<code class="prettyprint">vi</code>编辑器将打开crontab配置文件，然后使用’<code class="prettyprint">:wq!'</code>保存并关闭该文件。<br>
<pre class="prettyprint"># crontab -e<br>
30 01 * * * /usr/scripts/rsync_svnvmback.sh >/dev/null 2>&1<br>
</pre><br>
注意：在这里，我们有一个名为“rsync_svnbackup.sh”的bash脚本，每天（周一到周日）凌晨1点30分执行。一旦任务被执行，Cron就会向特定的用户发送一封关于任务状态的通知邮件，无论是成功还是失败。如果不需要通知，那么我们可以在脚本的最后使用<code class="prettyprint">>/dev/null 2>&amp;1</code>命令来禁用它，它将使所有的通知无效。<br>
<h4>2. 如何列出crontab任务？</h4>使用下面的命令列出我们添加到crontab配置文件中的任务。这里，我们使用的是root账户。<br>
<pre class="prettyprint"># crontab -l<br>
30 01 * * * /usr/scripts/rsync_svnvmback.sh >/dev/null 2>&1<br>
</pre><br>
注意：<code class="prettyprint">'-l'</code>是列出当前登录的用户的crontab列表的选项。<br>
<h4>3. 如何以其他用户身份修改cronjob？</h4>比方说，我想以另一个名为“linuxteck”的用户修改crontab任务。<br>
<pre class="prettyprint"># crontab -u linuxteck -e<br>
30 01 * * * /usr/scripts/rsync_svnvmback.sh<br>
</pre><br>
注意：上述命令只能由高权限用户执行，比如“root用户或超级用户”，或者被赋予了特权的普通用户。这里‘-u’代表用户名，‘-e’选项代表编辑。<br>
<h4>4. 如何列出其他用户的crontab任务？</h4>下面的命令将显示其他用户（linuxteck）的任务列表。<br>
<pre class="prettyprint"># crontab -u linuxteck -l<br>
30 01 * * * /usr/scripts/rsync_svnvmback.sh<br>
</pre><br>
注意：记住，只有root/超级用户可以执行上述命令，或者具有相同权限的普通用户。<br>
<h4>5. 如何配置每分钟运行的cronjob？</h4>这个要求在实际中很少使用，但也有一些用例。举个例子：如果你使用<code class="prettyprint">rsync</code>脚本/命令从线上服务器同步备份，这样以来，备份服务器将每分钟从线上服务器获得更新。<br>
<pre class="prettyprint"># crontab -e<br>
* * * * * /usr/scripts/rsync_svnvmback.sh<br>
</pre><br>
注意：上述crontab任务（rsync_svnvmback.sh）将在全年每小时中的每一分钟运行。<br>
<h4>6. 如何配置一个每天运行两次的cronjob？</h4>这意味着一条命令/脚本在一天内将被执行两次。举个例子：一些公司在早上和晚上进行数据库备份，比方说早上6点和晚上8点。<br>
<pre class="prettyprint">00 06,20 * * * /usr/scripts/mysqldump.sh >/dev/null 2>&1<br>
</pre><br>
注意：在小时字段使用了逗号分隔值。这个脚本将在每天早上6点和晚上8点执行。正如第一个例子中提到的，用<code class="prettyprint">'>/dev/null 2>&amp;1'</code>命令来禁用通知。<br>
<h4>7. 如何配置每10分钟运行一次的cronjob？</h4>下面的任务可以连续每10分钟执行一次命令/脚本。<br>
<pre class="prettyprint">*/10 * * * * /usr/scripts/rsync_svnvmback.sh<br>
</pre><br>
注意：你可以根据你的要求调整为5分钟或10分钟等进行测试。<br>
<h4>8. 如何配置特定日期执行的cronjob？</h4>使用下面的配置，我们可以在特定的日子里执行cronjob。例如：你可以只在周五和周日的晚上11点运行备份脚本。<br>
<pre class="prettyprint">> 0 23 * * fri,sun /usr/scripts/rsync_svnvmback.sh<br>
</pre><br>
注意：在这里我使用了日期的简称并用逗号来分隔，而不是数字，这样用户就很容易读懂。如果你使用数字，一些系统上是0-6，一些是1-7。因此，许多初学者在配置“星期天”时感到困惑，到底该使用0还是7。实际上，‘0和7’都代表星期天。<br>
<h4>9. 如何配置在特定月份运行的cronjob？</h4>使用下面的配置，我们可以为在特定月份执行cronjob，例如：该脚本应该只在1月和7月的晚上11.00执行。<br>
<pre class="prettyprint">0 23 * jan,jul * /usr/scripts/rsync_svnvmback.sh<br>
</pre><br>
注意：crontab语法中第四字段是月份的名称。如果不止一个月份执行，则使用逗号来分隔。<br>
<h4>10. 如何在一行中连续运行多个cronjob？</h4>正常情况下，我们为不同的任务、不同的时间一个一个地添加crontab任务。实际上，我们可以在一个特定的时间添加多个任务，一个接一个地执行。例如：我有多个命令/脚本要在我的服务器上执行，即备份数据库、备份应用程序文件，然后压缩数据库和文件，并将这些tar文件推送到备份位置，然后从服务器上删除这些tar/archive文件，然后清理tmp文件，等等。这种情况下，如果我们同时执行所有的脚本，将极大地影响服务器的性能。例如，可能导致服务器的磁盘空间用完，内存、CPU和带宽的占用率会大幅升高，有时甚至使服务器失去响应。<br>
<br>这种情况下，我们可以在crontab中使用下面的方式，让脚本一个接一个地执行，例如：如果我们有5组脚本要在早上1点运行，那么第一个脚本将在1点开始运行，一旦完成，第二个就立即开始，以此类推。<br>
<br>常规做法：<br>
<pre class="prettyprint">00 01 * * * /usr/scripts/mysqldump.sh  <br>
00 02 * * * /usr/scripts/application_backup.sh  <br>
10 01 * * * /usr/scripts/tar_db_appfile.sh  <br>
30 01 * * * /usr/scripts/cp_tar_remote_server.sh  <br>
10 02 * * * /usr/scripts/tardelete.sh  <br>
30 02 * * * /usr/scripts/clean_tmp.sh<br>
</pre><br>
多个任务在一个crontab中执行：<br>
<pre class="prettyprint">00 01 * * * /usr/scripts/mysqldump.sh && /usr/scripts/application_backup.sh && /usr/scripts/tar_db_appfile.sh && /usr/scripts/cp_tar_remote_server.sh && /usr/scripts/tardelete.sh && /usr/scripts/clean_tmp.sh<br>
<br>
-OR-<br>
<br>
00 01 * * * /usr/scripts/mysqldump.sh; /usr/scripts/application_backup.sh; /usr/scripts/tar_db_appfile.sh; /usr/scripts/cp_tar_remote_server.sh; /usr/scripts/tardelete.sh; /usr/scripts/clean_tmp.sh<br>
</pre><br>
注意：双引号‘&&’和分号‘;’的区别是：‘&&’意味着作业将一个接一个地执行，而‘;’则表示无论前面的作业是否成功，第二或第三作业都将运行。<br>
<h4>11. 如何在cron中使用特殊字符？</h4>特殊字符是cron中用一个关键词替换其他字段来执行任务。我们可以在’@’后面接关键字，语法和含义如下。<br>
<pre class="prettyprint">关键字       等价于          含义  <br>
@yearly     0 0 1 1 *     --> 每年执行一次<br>
@monthly    0 0 1 * *     --> 每月执行一次<br>
@daily      0 0 * * *     --> 每天执行一次<br>
@hourly     0 * * * *     --> 每小时执行一次<br>
@reboot     --            --> 重启后执行一次<br>
</pre><br>
接下来我们用几个例子来说明关键字的使用方法。<br>
<h4>12. 如何使用@yearly的特殊字符配置cronjob？</h4>@yearly相当于‘0 0 1 1 *’。<br>
<pre class="prettyprint">@yearly /usr/scripts/yearly_archival.sh<br>
</pre><br>
注意：上面的crontab任务将执行脚本，把所有前一年的数据移到存档服务器中。它将在每年的第一个月（一月）的00:00执行。<br>
<h4>13. 如何使用@monthly特殊字符来配置cronjob？</h4>@monthly相当于‘0 0 1 * *’。<br>
<pre class="prettyprint">@monthly /usr/scripts/monthly-backup.sh<br>
</pre><br>
注意：上面的crontab任务将执行每月备份的脚本，它将在每月1日的00:00执行。<br>
<h4>14. 如何使用@daily特殊字符串配置cronjob？</h4>@daily相当于‘0 0 * * *’。<br>
<pre class="prettyprint">@daily /usr/scripts/daily-temp.sh<br>
</pre><br>
注意：上述crontab任务将执行daily-temp.sh的脚本，它将清除temp文件夹中所有的临时文件。任务将在每天的00:00执行。<br>
<h4>15. 如何使用@hourly特殊字符配置cronjob？</h4>@hourly相当于‘0 * * *’。<br>
<pre class="prettyprint">@hourly /usr/scripts/hourly_rsync_svnvmback.sh<br>
</pre><br>
注意：上述crontab任务将执行hourly_rsync_svnvmback.sh的脚本，它每小时将所有数据从线上服务器同步到备份服务器。<br>
<h4>16. 如何使用@reboot特殊字符在每次重启后执行一个脚本/命令？</h4>@reboot可以用来在每次重启服务器后执行一组命令/脚本。例如：在重启后，我们可以执行一个命令/脚本来检查服务的状态，如DNS、Apache状态等。<br>
<pre class="prettyprint">@reboot /usr/scripts/bootup_service_status.sh<br>
</pre><br>
注意：上述crontab脚本将在每次重启后执行。这里，我在脚本中加入了检查“httpd, named,dhcpd”等状态的命令，这样它就会显示所有服务的状态列表。<br>
<br>我希望这篇文章能够帮助你学习Linux中的crontab命令。欢迎把你的反馈/意见告诉我。<br>
<br>感谢阅读！<br>
<br>译文链接：<a href="https://tlanyan.pp.ua/basic-cron-command-in-linux-with-examples/" rel="nofollow" target="_blank">https://tlanyan.pp.ua/basic-cr ... ples/</a>
                                
                                                              
</div>
            