# 更新日志

## [1.3.20] - 2024-12-29

### 修复

- 修复添加字典时报错问题。
- 底层物理删除改为逻辑删除。

## [1.3.19] - 2024-12-17

### 修复

- 修复线上环境Linux ubuntu 系统下找回密码邮件发送失败的问题。

## [1.3.18] - 2024-12-17

### 新增

- 新增通过邮箱找回密码功能，找回的前提是已经在个人中心正确的设置了可以正常使用的邮箱账号！

- 发送邮件配置在后台的字典管理中配置邮箱相关配置。

## [1.3.17] - 2024-12-13

### 新增

- 自定义菜单, 该功能默认是关闭的，在1.3.17版本init命令初始化的时候会自动生成一个自定义菜单！

开启只需要在项目的settings.py中配置如下代码即可：

```python
BAYKE_SETTINGS = {
    'USE_MENU': True,
}
```

USE_MENU为是否使用自定义菜单，默认为False，如果为True，则使用自定义菜单，否则使用默认菜单。

开启自定义菜单后，会在系统菜单中看到一个二级菜单“菜单管理”，可以添加一级菜单和二级菜单，一级菜单不能关联权限及点击，二级菜单是实际的权限菜单，如果想让某个用户可以看到该菜单那么只需要分配模型的view权限给用户即可，那么改菜单只需要关联一个模型view权限即可。