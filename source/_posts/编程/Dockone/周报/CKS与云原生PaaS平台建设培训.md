
---
title: 'CKS与云原生PaaS平台建设培训'
categories: 
 - 编程
 - Dockone
 - 周报
headimg: 'https://picsum.photos/400/300?random=3448'
author: Dockone
comments: false
date: 2021-12-05 08:09:58
thumbnail: 'https://picsum.photos/400/300?random=3448'
---

<div>   
<br>Kubernetes安全专家认证（Certified Kubernetes Security Specialist），简称CKS。获得认证的Kubernetes安全专家具备丰富的知识、技能及最佳实践能力，能够在构建、部署和运行Kubernetes过程中保护基于容器的应用程序和Kubernetes平台。<br>
<br>PaaS课程讲师结合自身工作经验，带领学员深入理解云原生的本质及价值，学习整个生态产品，规划构建PaaS平台所需的全部知识，通过学习本课程，学员可以结合企业业务场景，组织架构，输出云原生应用架构升级，数字化转型方案设计能力。<br>
<br><h4>第一天</h4>CKS最新考纲解读与如何保护Kubernetes集群<br>
<ul><li>CKS考试大纲解读</li><li>概览：Kubernetes集群组件架构</li><li>概览：保护Kubernetes集群安全</li></ul><br>
<br>Kubernetes安全领域知识介绍<br>
<ul><li>Kubernetes的威胁模型/Kubernetes Threat modeling</li><li>什么是威胁模型/Threat modeling</li><li>Kubernetes集群中的威胁源</li><li>Kubernetes集群中的主要威胁</li><li><br>Kubernetes安全边界<br>
<ul><li>什么是安全边界（security boundaries）</li><li>安全边界（security boundaries）和信任边界（trust boundaries）</li><li>Kubernetes的安全边界</li><li>Linux系统的安全边界</li><li>网络的安全边界</li></ul></li><li><br>纵深防御/Defense in Depth<br>
<ul><li>Kubernetes审计介绍</li><li>Kubernetes集群的高可用性</li><li>管理Kubernetes秘钥</li><li>使用Vault管理秘钥</li><li>用Falco探测Kubernetes集群异常</li><li>Sysdig介绍</li></ul></li></ul><br>
<br>Kubernetes集群搭建/Cluster Setup<br>
<ul><li><br>使用网络策略NetworkPolicy限制集群网络访问<br>
<ul><li>实战：使用网络插件Calico，实现NetworkPolicy</li></ul></li><li><br>使用CIS基准来检查Kubernetes组件（kube-api-server、kube-scheduler、kubelet、etcd）的安全配置<br>
<ul><li>了解什么是CIS（Center for Internet Security）基准</li><li>安装和使用CIS Kubernetes Benchmark测试工具：kube-bench</li><li>使用kube-bench检测master及worker nodes的安全隐患配置</li></ul></li><li><br>Ingress的安全配置<br>
<ul><li>了解什么是Ingress</li><li>为Ingress配置自签名证书，建立TLS安全通信</li></ul></li><li><br>部署前验证Kubernetes二进制文件<br>
<ul><li>通过sha512sum验证Kubernetes二进制文件</li></ul></li></ul><br>
<br>Kubernetes集群安全强化/Cluster Hardening<br>
<ul><li><br>限制对Kubernetes API的访问<br>
<ul><li>Kubernetes的鉴权/Kubernetes authentication</li><li>Kubernetes的授权/Kubernetes authorization</li><li>Kubernetes的准入控制/Kubernetes Admission Control</li></ul></li><li><br>RBAC（基于角色的访问控制）<br>
<ul><li>了解什么是RBAC</li><li>RBAC的使用，创建ServiceAccount，Role/ClusterRole和RoleBinding/ClusterRoleBinding</li></ul></li><li><br>ServiceAccount的最佳安全实践<br>
<ul><li>禁用默认的ServiceAccount</li><li>对新创建的ServiceAccount应用最小权限原则</li></ul></li><li><br>升级Kubernetes<br>
<ul><li>使用kubeadm升级Kubernetes集群</li></ul></li></ul><br>
<br>系统强化/System Hardening<br>
<ul><li><br>减小系统的被攻击面<br>
<ul><li>去除不需要的系统软件模块</li></ul></li><li><br>限制对外网的访问<br>
<ul><li>使用防火墙保护主机</li><li>使用NetworkPolicy限制对外网的访问</li></ul></li><li><br>使用Linux系统安全模块<br>
<ul><li>使用AppArmor限制容器对资源的访问</li><li>使用Seccomp限制容器内进程的系统调用</li></ul></li></ul><br>
<br>最小化微服务漏洞/Minimize Microservice Vulnerabilities<br>
<ul><li><br>使用PSP，OPA，安全上下文提高安全性<br>
<ul><li>了解并配置Pod安全策略（PSP）</li><li>了解并配置OPA Gatekeeper</li><li>了解并配置Pod或容器安全上下文（securityContext）</li></ul></li><li><br>管理Kubernetes Secret<br>
<ul><li>使用Kubernetes Secret存储敏感信息</li></ul></li><li><br>在多租户环境中使用沙箱运行容器（例如gVisor，kata容器）<br>
<ul><li>了解为什么要部署沙箱</li><li>什么是gVisor？安装gVisor</li><li>配置RuntimeClass，使用gVisor运行Pod</li></ul></li><li><br>实现Pod和Pod之间的双向TLS认证<br>
<ul><li>了解什么是mTLS（mutual TLS）</li><li>使用mTLS进行安全通信</li></ul></li></ul><br>
<br><h4>第二天</h4>供应链安全<br>
<ul><li><br>容器安全<br>
<ul><li>选择尽可能小的基础镜像</li><li>对容器镜像进行签名和验证</li></ul></li><li><br>防止恶意容器创建<br>
<ul><li>通过黑名单/白名单来限制访问容器镜像仓库</li><li>了解准入控制器 Admission Control</li><li>了解并配置ImagePolicyWebhook</li></ul></li><li><br>分析文件及镜像安全隐患<br>
<ul><li>分析Dockerfile、Kubernetes yaml文件的安全隐患</li><li>使用工具扫描镜像漏洞，如trivy</li></ul></li></ul><br>
<br>监控、审计和运行时安全<br>
<ul><li><br>分析容器系统调用，检测恶意进程<br>
<ul><li>安装并使用Falco，进行运行时安全监控</li></ul></li><li><br>构建不可变容器（Immutable container）</li><li><br>Kubernetes审计<br>
<ul><li>开启Kubernetes审计日志</li><li>分析Kubernetes审计日志</li></ul></li></ul><br>
<br>Kubernetes常见漏洞/Kubernetes CVEs（Common Vulnerabilities and Exposures）<br>
<ul><li>检测和分析加密货币挖矿攻击（Crypto-Mining Attacks）</li><li>Kubernetes常见漏洞分析及应对方法</li><li>使用第三方工具扫描Kubernetes常见漏洞</li><li>CKS模拟题演练与解析</li></ul><br>
<br><h4>第三天：云原生技术解析</h4><ul><li>云原生价值</li><li>开放应用模型【OAM】</li><li>服务网格【Istio】</li><li>发布策略【OpenKruise】</li><li>PaaS平台建设实践</li></ul><br>
<br><h4>第四天：PaaS能力建设</h4><ul><li>制品管理</li><li>资源网络规划</li><li>编排部署</li><li>部署策略</li><li>灰度发布</li><li>监控日志</li><li>链路跟踪</li><li>运维平台</li><li>双活灾备</li><li>应用迁移</li></ul><br>
<br>第五天：高级特性&解决方案<br>
<ul><li>应用市场&模板商店</li><li>Serverless</li><li><br>主流大厂云原生能力全景<br>
<ul><li>阿里&华为&腾讯</li></ul></li><li><br>解决方案<br>
<ul><li>云原生应用上云方案</li><li>资源弹性及调度方案</li><li>云原生AI方案</li></ul></li><li><br>技术方案交流【Q&A】</li></ul><br>
<br>培训方式：线下授课
                                
                                                              
</div>
            