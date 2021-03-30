
---
title: '源码解读：KubeVela 是如何将 appfile 转换为 K8s 特定资源对象的'
categories: 
 - 编程
 - segmentfault
 - 用户
headimg: 'https://segmentfault.com/img/remote/1460000039740158'
author: segmentfault
comments: false
date: 2021-03-30 08:09:45
thumbnail: 'https://segmentfault.com/img/remote/1460000039740158'
---

<div>   
<p><strong>简介：</strong> KubeVela 是一个简单易用又高度可扩展的云原生应用管理引擎，是基于 Kubernetes 及阿里云与微软云共同发布的云原生应用开发模型 OAM 构建。本文主要目的是探索 KubeVela 如何将一个 appfile 文件转换为 K8s 中特定的资源对象。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740158" alt="1.png" title="1.png" referrerpolicy="no-referrer"></span></p><p>作者 | 樊大勇</p><p>KubeVela 是一个简单易用又高度可扩展的云原生应用管理引擎，是基于 Kubernetes 及阿里云与微软云共同发布的云原生应用开发模型 OAM 构建。</p><p>KubeVela 基于 OAM 模型构建了一套具体的实现，通过 Golang 编写，可以端到端地为用户构建云原生应用的平台，提供一个相对完整的解决方案。</p><p>KubeVela 项目自 2020 年 7 月份在社区里面发起，受到包括阿里、微软、Crossplane 等公司工程师在内的广大社区志愿者的欢迎，并一起投入到项目开发工作中。他们把在 OAM 实践里面的各种经验与教训，都总结沉淀到 KubeVela 项目中。</p><p>本文主要目的是探索 KubeVela 如何将一个 appfile 文件转换为 K8s 中特定的资源对象。</p><p>该过程总的来说分为两个阶段：</p><ol><li>appfile 转为 K8s 中的 application</li><li>application 转换为对应的 K8s 资源对象</li></ol><pre><code># vela.yaml
name: test
services:
  nginx:
    type: webservice
    image: nginx
    env:
    - name: NAME
      value: kubevela

    # svc trait
    svc:
      type: NodePort
      ports:
      - port: 80
        nodePort: 32017</code></pre><p>利用 vela up 命令可以完成部署。</p><h1>vela up 命令</h1><p>建议：在看 vela 命令行工具代码之前，先去简单了解一下 cobra 框架。</p><pre><code>// references/cli/up.go
// NewUpCommand will create command for applying an AppFile
func NewUpCommand(c types.Args, ioStream cmdutil.IOStreams) *cobra.Command &#123;
  cmd := &cobra.Command&#123;
    Use:                   "up",
    DisableFlagsInUseLine: true,
    Short:                 "Apply an appfile",
    Long:                  "Apply an appfile",
    Annotations: map[string]string&#123;
      types.TagCommandType: types.TypeStart,
    &#125;,
    PersistentPreRunE: func(cmd *cobra.Command, args []string) error &#123;
      return c.SetConfig()
    &#125;,
    RunE: func(cmd *cobra.Command, args []string) error &#123;
      velaEnv, err := GetEnv(cmd)
      if err != nil &#123;
        return err
      &#125;
      kubecli, err := c.GetClient()
      if err != nil &#123;
        return err
      &#125;

      o := &common.AppfileOptions&#123;
        Kubecli: kubecli,
        IO:      ioStream,
        Env:     velaEnv,
      &#125;
      filePath, err := cmd.Flags().GetString(appFilePath)
      if err != nil &#123;
        return err
      &#125;
      return o.Run(filePath, velaEnv.Namespace, c)
    &#125;,
  &#125;
  cmd.SetOut(ioStream.Out)

  cmd.Flags().StringP(appFilePath, "f", "", "specify file path for appfile")
  return cmd
&#125;</code></pre><p>上面源码展示的是 vela up 命令的入口。</p><p>在 PresistentPreRunE 函数中，通过调用 c.SetConfig() 完成 Kuberentes 配置信息 kubeconfig 的注入。</p><p>在 RunE 函数中：</p><ul><li>首先，获取 vela 的 env 变量，velaEnv.Namespace 对应 Kubernetes 的命名空间。</li><li>其次，获取 Kubernetes 的客户端，kubectl。</li><li>接着，利用 Kubernetes 客户端和 vleaEnv 来构建渲染 Appfile 需要的 AppfileOptions。</li><li><p>最后，调用 o.Run(filePath, velaEnv.Namespace, c)。</p><ul><li><p>该函数需要三个参数，其中 filePath 用于指定 appfile 的位置，velaEnv.Namespace 和 c 用来将渲染后的 Application 创建到指定命名空间。</p><ul><li>filePath: appfile 的路径</li><li>velaEnv.Namespace：对应 K8s 的 namespace</li><li>c：K8s 客户端</li></ul></li></ul></li></ul><h1>如何将一个 appfile 转为 Kubernetes 中的 Application</h1><ul><li>起点：appfile</li><li>终点：applicatioin</li><li><p>路径：appfile -> application (services -> component)</p><ul><li>comp[workload, traits]</li></ul></li></ul><h3>1. 起点：AppFile</h3><pre><code>// references/appfile/api/appfile.go
// AppFile defines the spec of KubeVela Appfile
type AppFile struct &#123;
  Name       string             `json:"name"`
  CreateTime time.Time          `json:"createTime,omitempty"`
  UpdateTime time.Time          `json:"updateTime,omitempty"`
  Services   map[string]Service `json:"services"`
  Secrets    map[string]string  `json:"secrets,omitempty"`

  configGetter config.Store
  initialized  bool
&#125;

// NewAppFile init an empty AppFile struct
func NewAppFile() *AppFile &#123;
  return &AppFile&#123;
    Services:     make(map[string]Service),
    Secrets:      make(map[string]string),
    configGetter: &config.Local&#123;&#125;,
  &#125;
&#125;</code></pre><pre><code>// references/appfile/api/service.go
// Service defines the service spec for AppFile, it will contain all related information including OAM component, traits, source to image, etc...
type Service map[string]interface&#123;&#125;</code></pre><p>上面两段代码是 AppFile 在客户端的声明，vela 会将指定路径的 yaml 文件读取后，赋值给一个 AppFile。</p><pre><code>// references/appfile/api/appfile.go
// LoadFromFile will read the file and load the AppFile struct
func LoadFromFile(filename string) (*AppFile, error) &#123;
  b, err := ioutil.ReadFile(filepath.Clean(filename))
  if err != nil &#123;
    return nil, err
  &#125;
  af := NewAppFile()
  // Add JSON format appfile support
  ext := filepath.Ext(filename)
  switch ext &#123;
  case ".yaml", ".yml":
    err = yaml.Unmarshal(b, af)
  case ".json":
    af, err = JSONToYaml(b, af)
  default:
    if json.Valid(b) &#123;
      af, err = JSONToYaml(b, af)
    &#125; else &#123;
      err = yaml.Unmarshal(b, af)
    &#125;
  &#125;
  if err != nil &#123;
    return nil, err
  &#125;
  return af, nil
&#125;</code></pre><p>下面为读取 vela.yaml 文件后，加载到 AppFile 中的数据：</p><pre><code># vela.yaml
name: test
services:
  nginx:
    type: webservice
    image: nginx
    env:
    - name: NAME
      value: kubevela

    # svc trait
    svc:
      type: NodePort
      ports:
      - port: 80
        nodePort: 32017</code></pre><pre><code>Name: test
CreateTime: 0001-01-01 00:00:00 +0000 UTC
UpdateTime: 0001-01-01 00:00:00 +0000 UTC
Services： map[
             nginx: map[
               env: [map[name: NAME value: kubevela]] 
               image: nginx 
               svc: map[ports: [map[nodePort: 32017 port: 80]] type: NodePort] 
               type: webservice
            ]
          ]
Secrets    map[]
configGetter: 0x447abd0 
initialized: false</code></pre><h3>2. 终点：application</h3><pre><code>// apis/core.oam.dev/application_types.go
type Application struct &#123;
  metav1.TypeMeta   `json:",inline"`
  metav1.ObjectMeta `json:"metadata,omitempty"`

  Spec   ApplicationSpec `json:"spec,omitempty"`
  Status AppStatus       `json:"status,omitempty"`
&#125;

// ApplicationSpec is the spec of Application
type ApplicationSpec struct &#123;
  Components []ApplicationComponent `json:"components"`

  // TODO(wonderflow): we should have application level scopes supported here

  // RolloutPlan is the details on how to rollout the resources
  // The controller simply replace the old resources with the new one if there is no rollout plan involved
  // +optional
  RolloutPlan *v1alpha1.RolloutPlan `json:"rolloutPlan,omitempty"`
&#125;</code></pre><p>上面代码，为 Application 的声明，结合 .vela/deploy.yaml（见下面代码），可以看出，要将一个 AppFile 渲染为 Application 主要就是将 AppFile 的 Services 转化为 Application 的 Components。</p><pre><code># .vela/deploy.yaml
apiVersion: core.oam.dev/v1alpha2
kind: Application
metadata:
  creationTimestamp: null
  name: test
  namespace: default
spec:
  components:
  - name: nginx
    scopes:
      healthscopes.core.oam.dev: test-default-health
    settings:
      env:
      - name: NAME
        value: kubevela
      image: nginx
    traits:
    - name: svc
      properties:
        ports:
        - nodePort: 32017
          port: 80
        type: NodePort
    type: webservice
status: &#123;&#125;</code></pre><h3>3. 路径：Services -> Components</h3><p>结合以上内容可以看出，将 Appfile 转化为 Application 主要是将 Services 渲染为 Components。</p><pre><code>// references/appfile/api/appfile.go
// BuildOAMApplication renders Appfile into Application, Scopes and other K8s Resources.
func (app *AppFile) BuildOAMApplication(env *types.EnvMeta, io cmdutil.IOStreams, tm template.Manager, silence bool) (*v1alpha2.Application, []oam.Object, error) &#123;
  ...
  servApp := new(v1alpha2.Application)
  servApp.SetNamespace(env.Namespace)
  servApp.SetName(app.Name)
  servApp.Spec.Components = []v1alpha2.ApplicationComponent&#123;&#125;
  for serviceName, svc := range app.GetServices() &#123;
    ...
    // 完成 Service 到 Component 的转化
    comp, err := svc.RenderServiceToApplicationComponent(tm, serviceName)
    if err != nil &#123;
      return nil, nil, err
    &#125;
    servApp.Spec.Components = append(servApp.Spec.Components, comp)
  &#125;
  servApp.SetGroupVersionKind(v1alpha2.SchemeGroupVersion.WithKind("Application"))
  auxiliaryObjects = append(auxiliaryObjects, addDefaultHealthScopeToApplication(servApp))
  return servApp, auxiliaryObjects, nil
&#125;</code></pre><p>上面的代码是 vela 将 Appfile 转化为 Application 代码实现的位置。其中 comp, err := svc.RenderServiceToApplicationComponent(tm, serviceName) 完成 Service 到 Component 的转化。</p><pre><code>// references/appfile/api/service.go
// RenderServiceToApplicationComponent render all capabilities of a service to CUE values to KubeVela Application.
func (s Service) RenderServiceToApplicationComponent(tm template.Manager, serviceName string) (v1alpha2.ApplicationComponent, error) &#123;

  // sort out configs by workload/trait
  workloadKeys := map[string]interface&#123;&#125;&#123;&#125;
  var traits []v1alpha2.ApplicationTrait

  wtype := s.GetType()
  comp := v1alpha2.ApplicationComponent&#123;
    Name:         serviceName,
    WorkloadType: wtype,
  &#125;

  for k, v := range s.GetApplicationConfig() &#123;
    // 判断是否为 trait
    if tm.IsTrait(k) &#123;
      trait := v1alpha2.ApplicationTrait&#123;
        Name: k,
      &#125;
      ....
      // 如果是 triat 加入 traits 中
      traits = append(traits, trait)
      continue
    &#125;
    workloadKeys[k] = v
  &#125;

  // Handle workloadKeys to settings
  settings := &runtime.RawExte nsion&#123;&#125;
  pt, err := json.Marshal(workloadKeys)
  if err != nil &#123;
    return comp, err
  &#125;
  if err := settings.UnmarshalJSON(pt); err != nil &#123;
    return comp, err
  &#125;
  comp.Settings = *settings

  if len(traits) > 0 &#123;
    comp.Traits = traits
  &#125;

  return comp, nil
&#125;</code></pre><h3>4. 总结</h3><p>执行 vela up 命令，渲染 appfile 为 Application，将数据写入到 .vela/deploy.yaml 中，并在 K8s 中创建。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740160" alt="2.png" title="2.png" referrerpolicy="no-referrer"></span></p><h1>Application 是如何转换为对应 K8s 资源对象</h1><ul><li>起点：Application</li><li>中点：ApplicationConfiguration, Component</li><li>终点：Deployment, Service</li><li><p>路径：</p><ul><li>application_controller</li><li>applicationconfiguration controller</li></ul></li></ul><blockquote><p><strong>【建议】</strong>> 了解一下内容：> - client-to</p><ul><li>controller-runtime</li><li>operator</li></ul></blockquote><h3>1. Application</h3><pre><code># 获取集群中的 Application
$ kubectl get application
NAMESPACE   NAME   AGE default    test   24h</code></pre><h3>2. ApplicationConfiguration 和 Component</h3><p>当 application controller 获取到 Application 资源对象之后，会根据其内容创建出对应的 ApplicationConfiguration 和 Component。</p><pre><code># 获取 ApplicationConfiguration 和 Component
$ kubectl get ApplicationConfiguration,Component
NAME                                         AGE
applicationconfiguration.core.oam.dev/test   24h

NAME                           WORKLOAD-KIND   AGE
component.core.oam.dev/nginx   Deployment      24h</code></pre><p>ApplicationiConfiguration 中以名字的方式引入 Component：</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740161" alt="3.png" title="3.png" referrerpolicy="no-referrer"></span></p><h3>3. application controller</h3><h5>基本逻辑：</h5><ul><li>获取一个 Application 资源对象。</li><li>将 Application 资源对象渲染为 ApplicationConfiguration 和 Component。</li><li>创建 ApplicationConfiguration 和 Component 资源对象。</li></ul><h5>代码：</h5><pre><code>// pkg/controller/core.oam.dev/v1alpha2/application/application_controller.go

// Reconcile process app event
func (r *Reconciler) Reconcile(req ctrl.Request) (ctrl.Result, error) &#123;
  ctx := context.Background()
  applog := r.Log.WithValues("application", req.NamespacedName)
  
  // 1. 获取 Application
  app := new(v1alpha2.Application)
  if err := r.Get(ctx, client.ObjectKey&#123;
    Name:      req.Name,
    Namespace: req.Namespace,
  &#125;, app); err != nil &#123;
    ...
  &#125;

  ...

  // 2. 将 Application 转换为 ApplicationConfiguration 和 Component
  handler := &appHandler&#123;r, app, applog&#125;
  ...
  appParser := appfile.NewApplicationParser(r.Client, r.dm)
  ...
  appfile, err := appParser.GenerateAppFile(ctx, app.Name, app)
  ...
  ac, comps, err := appParser.GenerateApplicationConfiguration(appfile, app.Namespace)
  ...
  
  // 3. 在集群中创建 ApplicationConfiguration 和 Component 
  // apply appConfig & component to the cluster
  if err := handler.apply(ctx, ac, comps); err != nil &#123;
    applog.Error(err, "[Handle apply]")
    app.Status.SetConditions(errorCondition("Applied", err))
    return handler.handleErr(err)
  &#125;

  ...
  return ctrl.Result&#123;&#125;, r.UpdateStatus(ctx, app)
&#125;</code></pre><h3>4. applicationconfiguration controller</h3><h5>基本逻辑：</h5><ul><li>获取 ApplicationConfiguration 资源对象。</li><li>循环遍历，获取每一个 Component 并将 workload 和 trait 渲染为对应的 K8s 资源对象。</li><li>创建对应的 K8s 资源对象。</li></ul><h5>代码：</h5><pre><code>// pkg/controller/core.oam.dev/v1alpha2/applicationcinfiguratioin/applicationconfiguratioin.go

// Reconcile an OAM ApplicationConfigurations by rendering and instantiating its
// Components and Traits.
func (r *OAMApplicationReconciler) Reconcile(req reconcile.Request) (reconcile.Result, error) &#123;
  ...
  ac := &v1alpha2.ApplicationConfiguration&#123;&#125;
  // 1. 获取 ApplicationConfiguration
  if err := r.client.Get(ctx, req.NamespacedName, ac); err != nil &#123;
    ...
  &#125;
  return r.ACReconcile(ctx, ac, log)
&#125;

// ACReconcile contains all the reconcile logic of an AC, it can be used by other controller
func (r *OAMApplicationReconciler) ACReconcile(ctx context.Context, ac *v1alpha2.ApplicationConfiguration,
  log logging.Logger) (result reconcile.Result, returnErr error) &#123;
  
  ...
  // 2. 渲染
  // 此处 workloads 包含所有Component对应的的 workload 和 tratis 的 k8s 资源对象
  workloads, depStatus, err := r.components.Render(ctx, ac)
  ...
  
  applyOpts := []apply.ApplyOption&#123;apply.MustBeControllableBy(ac.GetUID()), applyOnceOnly(ac, r.applyOnceOnlyMode, log)&#125;
  
  // 3. 创建 workload 和 traits 对应的 k8s 资源对象
  if err := r.workloads.Apply(ctx, ac.Status.Workloads, workloads, applyOpts...); err != nil &#123;
    ...
  &#125;
  
  ...

  // the defer function will do the final status update
  return reconcile.Result&#123;RequeueAfter: waitTime&#125;, nil
&#125;</code></pre><h3>5. 总结</h3><p>当 vela up 将一个 AppFile 渲染为一个 Application 后，后续的流程由 application controller 和 applicationconfiguration controller 完成。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039740159" alt="4.png" title="4.png" referrerpolicy="no-referrer"></span></p><h3>作者简介</h3><p>樊大勇，华胜天成研发工程师，GitHub ID：@just-do1。</p><p><a href="https://developer.aliyun.com/article/783169?utm_content=g_1000257747" rel="nofollow">原文链接</a><br>本文为阿里云原创内容，未经允许不得转载。</p>  
</div>
            