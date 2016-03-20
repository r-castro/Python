;; init.el --- Emacs configuration

;; INSTALL PACKAGES
;;-------------------------------


(require 'package)

(add-to-list 'package-archives
	     '("melpa" . "http://melpa.org/packages/")t)

(package-initialize)
(when (not package-archive-contents)
  (package-refresh-contents))

(defvar myPackages
  '(better-defaults
    ein
    elpy
    flycheck
    material-theme
    py-autopep8))

(elpy-enable)
(setq elpy-rpc-python-command "python3")
(setq python-shell-interpreter "ipython3")

(when (require 'flycheck nil t)
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))

(require 'py-autopep8)
(add-hook 'elpy-mode-hook 'py-autopep8-enable-on-save)

(mapc #'(lambda (package)
	  (unless (package-installed-p package)
	    (package-install package)))
      myPackages)

;; BASIC CONFIGURATION
;; -----------------------------------------------------

(setq inhibit-startup-message t)
(load-theme 'ample t t)
(load-theme 'ample-flat t t)
(load-theme 'ample-light t t)
;; choose one to enable
(enable-theme 'ample)
;; (enable-theme 'ample-flat)
;; (enable-theme 'ample-light)
(global-linum-mode t)
(setq linum-format "%4d ")
(electric-pair-mode +1)


(add-to-list 'load-path "~/.emacs.d/site-lisp/magit/lisp")
(require 'magit)

(with-eval-after-load 'info
  (info-initialize)
  (add-to-list 'Info-directory-list
                              "~/.emacs.d/site-lisp/magit/Documentation/"))
