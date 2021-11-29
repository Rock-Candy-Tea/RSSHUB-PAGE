
---
title: '必备小技巧：教您如何在Windows 11中创建本地账户'
categories: 
 - 新媒体
 - cnBeta
 - 最新
headimg: 'https://static.cnbetacdn.com/article/2021/1129/f6442eb1cf11a8e.png'
author: cnBeta
comments: false
date: Mon, 29 Nov 2021 01:56:34 GMT
thumbnail: 'https://static.cnbetacdn.com/article/2021/1129/f6442eb1cf11a8e.png'
---

<div>   
微软在Windows 11中，大力推广微软在线账户，在默认情况下大家得通过微软账号来登录到Windows
11。但很多情况下，本地账户会更加适合使用，例如在公用电脑上，又例如在微软服务器不畅通的环境下，或者你就是不想使用微软在线服务这类情况等等。但要如何在Windows
11中切换到本地账户？这就来分享几种方法。<br>
 <p><strong>用CMD添加本地账户</strong></p><p>这可能是最简单的一种方法。在<a data-link="1" href="https://microsoft.pvxt.net/x9Vg1" target="_blank">Windows</a> 11中，搜索CMD，然后使用管理员权限打开命令提示符。</p><p>接着，在CMD中输入以下命令：</p><p>net user username password /add</p><p>注意，其中“username”是你的账户名，“password”是账户的密码，这两项可以自定义。按下回车键，一个本地账户就创建完毕了。</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/f6442eb1cf11a8e.png" referrerpolicy="no-referrer"><br>如图，用户名是“tset”，密码是“123”</p><p>在设置中，我们可以查看到这个本地账户，对其进行管理。</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/62635eb6ea984a2.png" referrerpolicy="no-referrer"><br></p><p><strong>用设置面板添加本地账户</strong></p><p>这个方法步骤没有那么简单，不过可能会更加直白，适合不喜欢用命令行的用户。</p><p>我们打开Windows 11的设置面板。即可找到账户的相关选项。在家庭和其他用户一栏中，点进去后可以发现添加其他用户的选项，点击即可。</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/ae0d898aef369de.png" referrerpolicy="no-referrer"><br></p><p>接着，Windows 11会弹窗询问该用户使用怎样的方法来登录到系统，这里选择不知道该用户的登录信息。接着，即可看到不使用<a data-link="1" href="https://c.duomai.com/track.php?site_id=242986&euid=&t=https://www.microsoftstore.com.cn/" target="_blank">微软</a>账户添加用户的选项，到这里我们就可以添加一个本地账户了。</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/07a8a9c97159ac5.png" referrerpolicy="no-referrer"><br></p><p><img src="https://static.cnbetacdn.com/article/2021/1129/63449190f724998.png" referrerpolicy="no-referrer"><br></p><p>完成用户名和密码以及密保问题设置后，回到设置面板，即可发现这个本地账户。</p><p><strong>用用户账户管理页面添加本地账户</strong></p><p>在Windows 11中，通过搜索找出“运行”，然后运行以下命令：</p><p>netplwiz</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/819b5625fae320c.png" referrerpolicy="no-referrer"><br></p><p>接着，即可看到用户账户的管理页面。在这里，我们可以看到当前系统中的用户账户，当然也可以自行添加账户。点击下方的“添加”，就会进入到添加新用户的流程。</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/d0df1291b6c240c.png" referrerpolicy="no-referrer"><br></p><p>在弹出的窗口当中（必须吐槽一下这个窗口还是Windows 10风格），可以在下方选择不使用微软账户登录，接着按部就班填写用户名和密码等信息，就完成了。</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/39a65b53652015f.png" referrerpolicy="no-referrer"><br></p><p><strong>要如何让本地账户拥有管理员权限？要如何删除本地账户？</strong></p><p>添加了本地账户后，可能该账户还是被分配在“user”组，能做的事情有限。同时，如果我们不想要某个账户了，也得将它删掉，要怎么做？</p><p>其实这两个功能是放在一起的。在设置面板中，我们进入到账户的相关设置，在家庭和其他用户的页面中，就可以看到本地账户的列表了。</p><p><img src="https://static.cnbetacdn.com/article/2021/1129/7012e231b0d8eb9.png" referrerpolicy="no-referrer"><br></p><p>点击某个本地账户，即可看到改变权限以及删除数据的选项，操作即可。</p><p><strong>总结</strong></p><p>总的来说，本地账户在实际使用场景中，仍有相当多的用途，微软推行网络账户登录Windows 11系统，似乎是有点操之过急了。如果你需要使用本地账户登录Windows 11，不妨尝试一下上文的方法，有其他别的方法也欢迎在评论区和大家分享！</p>   
</div>
            