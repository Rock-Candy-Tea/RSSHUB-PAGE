
---
title: 'GitLab CI_CD (www.cnblogs.com)'
categories: 
 - 编程
 - 技术头条
 - 最新分享
headimg: 'https://picsum.photos/400/300?random=1320'
author: 技术头条
comments: false
date: 2021-05-24 00:15:54
thumbnail: 'https://picsum.photos/400/300?random=1320'
---

<div>   
GitLab CI/CD 是一个内置在GitLab中的工具，用于通过持续方法进行软件开发：
Continuous Integration (CI)  持续集成；
Continuous Delivery (CD)     持续交付；
Continuous Deployment (CD)   持续部署；

持续集成的工作原理是将小的代码块推送到Git仓库中托管的应用程序代码库中，并且每次推送时，都要运行一系列脚本来构建、测试和验证代码更改，然后再将其合并到主分支中。

持续交付和部署相当于更进一步的CI，可以在每次推送到仓库默认分支的同时将应用程序部署到生产环境。

这些方法使得可以在开发周期的早期发现bugs和errors，从而确保部署到生产环境的所有代码都符合为应用程序建立的代码标准。

GitLab CI/CD 由一个名为 .gitlab-ci.yml 的文件进行配置，改文件位于仓库的根目录下。文件中指定的脚本由GitLab Runner执行。
    
</div>
            