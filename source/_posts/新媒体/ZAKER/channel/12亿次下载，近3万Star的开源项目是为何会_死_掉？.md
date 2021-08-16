
---
title: '1.2亿次下载，近3万Star的开源项目是为何会_死_掉？'
categories: 
 - 新媒体
 - ZAKER
 - channel
headimg: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202108/6119ba998e9f09137a610b4d_1024.jpg'
author: ZAKER
comments: false
date: Mon, 16 Aug 2021 03:45:00 GMT
thumbnail: 'https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202108/6119ba998e9f09137a610b4d_1024.jpg'
---

<div>   
<p>整理 | 孙胜 </p><p>出品 | CSDN（ID：CSDNnews）</p><p>Faker 是一个流行的模拟数据生成库，程序员只需简单地几步操作，就可以在浏览器和 Node.js 中生成大量的假数据，GitHub 的 Star 已超过 25000 星，但是 Faker 的开发人员 Fran ois Zaninotto 计划放弃对 Faker 更新维护。根据 GitHub 的数据显示，最近一次更新在 2020 年 12 月 11 日。</p><p></p><div class="img_box" id="id_imagebox_0" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_0" data-original="http://zkres2.myzaker.com/202108/6119ba998e9f09137a610b4d_1024.jpg" data-height="632" data-width="1333" src="https://cors.zfour.workers.dev/?http://zkres2.myzaker.com/202108/6119ba998e9f09137a610b4d_1024.jpg" referrerpolicy="no-referrer"></div></div><strong>Faker 意外诞生</strong><p></p><p><strong></strong></p><p>Faker 诞生很意外，Fran ois Zaninotto 需要为他的项目生成模拟数据，于是就在 2011 年 10 月开发了 Faker 项目 。由于 Faker 能产生大量的模拟逼真的数据，因此 Faker 在 PHP 社区被很多开源爱好者使用并获得好评。据 Fran ois Zaninotto 在博文中透露，截至 2020 年 10 月已有 450 多个贡献者（感谢他们的付出），被 713k 个项目所依赖。</p><p><?php// use the factory to create a FakerGenerator instance$faker = FakerFactory::create ( ) ;// generate data by accessing propertiesecho $faker->name;// 'Lucy Cechtelar';echo $faker->address;// "426 Jordy Lodge// Cartwrightshire, SC 88120-6700"echo $faker->text;// Dolores sit sint laboriosam dolorem culpa et autem. Beatae nam sunt fugit// et sit et mollitia sed.// Fuga deserunt tempora facere magni omnis. Omnis quia temporibus laudantium// sit minima sint</p><p><strong> Faker 存在设计瑕疵</strong></p><p><strong>Faker 维护太难了</strong></p><p><strong></strong></p><p>作者认为维护这个 Faker 太难了，因为 Faker 很多模拟数据都是从别的地方粘贴复制过来的，并受到版权法律保护，还有用户提交的 PR 都是作者看不懂的语种，因此他无法辨析数据的优劣，出于版权等风险考虑，他最终关闭了许多 PR，并盲目地合并了部分其他 PR。最主要原因是 Fran ois Zaninotto 没有时间去维护 Faker，而且他已经有 5 年时间没有写过一行 PHP 代码了。</p><p>有人提议将 Faker 移交到专门维护项目的组织， Fran ois Zaninotto 拒绝了，他认为这是在 " 诋毁 " 一个 25,000 Star 项目的声誉。</p><p><strong>Faker 使命完成了</strong></p><p><strong></strong></p><div class="img_box" id="id_imagebox_1" onclick><div class="content_img_div perview_img_div"><img class="lazy opacity_0 " id="img_1" data-original="http://zkres1.myzaker.com/202108/6119ba998e9f09137a610b4e_1024.jpg" data-height="273" data-width="720" src="https://cors.zfour.workers.dev/?http://zkres1.myzaker.com/202108/6119ba998e9f09137a610b4e_1024.jpg" referrerpolicy="no-referrer"></div></div>所以 Fran ois Zaninotto 决定 " 退休 "，意味着 Fran ois Zaninotto 不会接受新的 PR，不会合并现有的 PR，不会发布新版本，也不会接受新的维护者，将完全禁用来自 Faker 存储库的通知，并删除收件箱中所有与 Faker 相关的消息的存档——这对地球来说又是一个好举措。他认为这个决定伤害了那些为 Faker 付出时间和工作的贡献者，他对此深表歉意，另外他认为这个举动符合 PHP 社区的利益。<p></p><p>Fran ois Zaninotto 最后表示："Faker 仍然可以在 Packagist 上使用，只要您不升级 PHP 版本，它就会继续工作。相信其他人很快就会发布一个新的库来代替 Faker，它会比 Faker 好得多，而且会发展得更快。"</p><p>最后，屏幕前的你使用过 Faker 项目吗？你要是原开发者会放弃这个项目吗？</p><p>参考链接：</p><p>https://marmelab.com/blog/2020/10/21/sunsetting-faker.html</p><div id="recommend_bottom"></div><div id="article_bottom"></div>  
</div>
            