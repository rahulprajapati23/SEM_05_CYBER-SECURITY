# Reset Root Password (RHEL 9)

Follow these steps to reset the root password if it is lost or forgotten.

## 1. Reboot and Interrupt GRUB
*   Reboot the server (send `Ctrl+Alt+Del` or hard reset).
*   At the **GRUB menu**, press any key (except Enter) immediately to stop the countdown.

## 2. Edit Rescue Kernel
*   Select the entry for the **rescue kernel** (or the standard kernel if rescue is missing).
*   Press **`e`** to edit the selected boot entry.
*   Find the line starting with `linux` (it ends with `quiet` or similar).
*   **Remove** any `console=` entries (e.g., `console=tty0`) if present.
*   At the **end of the line**, add:
    ```bash
    rd.break
    ```
*   Press **`Ctrl + x`** to boot into emergency mode.

## 3. Remount Filesystem
At the `switch_root:/#` prompt, the file system is mounted as read-only. You must remount it as read-write.
```bash
mount -o remount,rw /sysroot
```

## 4. Change Root (Chroot)
Switch into the system root environment:
```bash
chroot /sysroot
```

## 5. Reset Password
Run the password command to set a new root password:
```bash
passwd root
```
*(Enter the new password twice when prompted)*

## 6. Force SELinux Relabeling
This step is critical. If skipped, you may not be able to log in.
```bash
touch /.autorelabel
```

## 7. Exit and Reboot
Type `exit` twice to leave the chroot environment and reboot the system.
```bash
exit
exit
```
*The system will take a few moments to relabel SELinux contexts before booting.*
